# Fitness App - User Management

## Описание

Этот проект представляет собой систему управления пользователями для фитнес-приложения, позволяющую пользователям регистрироваться, входить в систему, управлять своими профилями и подписками.

## Модели

### User

Модель `User` расширяет стандартную модель `AbstractUser` и включает в себя дополнительные атрибуты для управления личной информацией и фитнес-целями:

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fitness_goal = models.CharField(max_length=50, choices=[('Lose Weight', 'Lose Weight'), ('Build Muscle', 'Build Muscle'), ('Stay Fit', 'Stay Fit')], blank=True)
    last_login_date = models.DateTimeField(null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(default=False)
    subscription = models.OneToOneField('Subscription', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_subscription')
    current_training_plan = models.ForeignKey('exercise_management.TrainingPlan', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_current_training_plan')
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)

    def calculate_bmi(self):
        if self.weight and self.height:
            return self.weight / ((self.height / 100) ** 2)
        return None