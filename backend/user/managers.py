from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email"))

    def create_user(self, first_name, last_name, email, password, age=None, weight=None, **extra_fields):
        if not first_name:
            raise ValueError(_("Users must submit a first name"))
        
        if not last_name:
            raise ValueError(_("Users must submit a last name"))

        if age is not None and age < 0:
            raise ValueError(_("Age must be a positive number"))
        
        if weight is not None and weight < 0:
            raise ValueError(_("Weight must be a positive number"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User: an email address is required"))

        extra_fields.setdefault("is_active", True)  # Убедитесь, что пользователь активен
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,  
            weight=weight,
            **extra_fields
        )

        user.set_password(password)

        try:
            user.save()
        except Exception as e:
            raise ValueError(_("Error saving user: ") + str(e))

        return user

    def create_superuser(self, first_name, last_name, email, password, age=None, weight=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        
        if not password:
            raise ValueError(_("Superusers must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin User: an email address is required"))

        user = self.create_user(first_name, last_name, email, password, age=age, weight=weight, **extra_fields)
        return user
