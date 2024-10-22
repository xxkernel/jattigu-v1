# serializers.py

from datetime import timedelta, timezone
from .models import Subscription
from rest_framework import serializers
from django.db import models
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer as BaseUserSerializer

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'date_of_birth', 'gender', 'weight', 'height', 'fitness_goal']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'is_staff', 'is_active', 'date_joined', 
                  'date_of_birth', 'gender', 'weight', 'height', 'fitness_goal', 'last_login_date', 
                  'is_premium', 'subscription', 'current_training_plan', 'groups', 'user_permissions']

class UpdateUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'weight', 'height', 'fitness_goal', 'is_premium']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [ 'user', 'type', 'price', 'active_until', 'auto_renew', 'start_date']
