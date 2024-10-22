from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating a new user, including custom fields like age, weight, and fitness goals.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "email", 
            "first_name", 
            "last_name", 
            "age", 
            "gender", 
            "weight", 
            "height", 
            "fitness_goal"
        ]
        error_class = "error"

class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating user details, including custom fields like age, weight, and fitness goals.
    """
    class Meta(UserChangeForm.Meta):
        model = User
        fields = [
            "email", 
            "first_name", 
            "last_name", 
            "age", 
            "gender", 
            "weight", 
            "height", 
            "fitness_goal"
        ]
        error_class = "error"
