# user_management/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import User, Subscription
from .forms import RegistrationForm, LoginForm
from django.contrib import messages


# Регистрация
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# Вход
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Вы вошли в систему.")
                return redirect('home')
            else:
                messages.error(request, "Неверные данные для входа.")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


# Выход
def logout_view(request):
    logout(request)
    messages.success(request, "Вы вышли из системы.")
    return redirect('login')



# Профиль пользователя
@login_required
def profile_view(request):
    user = request.user
    bmi = user.calculate_bmi() if user.calculate_bmi() else "BMI не рассчитан"
    subscription = user.subscription
    return render(request, 'profile/profile.html', {
        'user': user,
        'bmi': bmi,
        'subscription': subscription,
        'days_left': subscription.days_left() if subscription else None,
    })


# Просмотр подписки
@login_required
def subscription_view(request):
    subscription = request.user.subscription
    if subscription is None:
        messages.info(request, "У вас нет активной подписки.")
    return render(request, 'profile/subscription.html', {'subscription': subscription})

# # Продление подписки
# @login_required
# def extend_subscription_view(request, duration_days=30):
#     subscription = request.user.subscription
#     if subscription:
#         subscription.extend_subscription(duration_days)
#         messages.success(request, f"Подписка продлена на {duration_days} дней.")
#     else:
#         messages.error(request, "Не удалось продлить подписку.")
#     return redirect('subscription')