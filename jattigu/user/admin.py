from django.contrib import admin
from .models import User, Subscription

class SubscriptionInline(admin.StackedInline):
    model = Subscription
    extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_premium')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    
    # Добавление возможности редактировать подписки прямо в форме пользователя
    inlines = [SubscriptionInline]

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'price', 'active_until', 'auto_renew', 'start_date')
    list_filter = ('type',)
    search_fields = ('user__email',)  # Поиск по email пользователя
    ordering = ('-start_date',)

