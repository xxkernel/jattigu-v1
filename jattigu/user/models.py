from datetime import timedelta, timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined =  models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)

    # Атрибуты для фитнес-целей
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fitness_goal = models.CharField(max_length=50, choices=[('Lose Weight', 'Lose Weight'), ('Build Muscle', 'Build Muscle'), ('Stay Fit', 'Stay Fit')], blank=True)

    # Атрибуты активности
    last_login_date = models.DateTimeField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)

    # Атрибуты для связи с подпиской и планами
    subscription = models.OneToOneField('Subscription', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_subscription')
    current_training_plan = models.ForeignKey('exercise_management.TrainingPlan', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_current_training_plan')

    # Измененные related_name для избежания конфликта
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Уникальное имя для предотвращения конфликта
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Уникальное имя для предотвращения конфликта
        blank=True,
    )

    def calculate_bmi(self):
        if self.weight and self.height:
            return self.weight / ((self.height / 100) ** 2)
        return None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    




class Subscription(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='subscription_detail')
    type = models.CharField(max_length=50, choices=[('Free', 'Free'), ('Premium', 'Premium')])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    active_until = models.DateField(null=True, blank=True)
    auto_renew = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)

    def is_active(self):
        return self.active_until >= timezone.now().date() if self.active_until else False

    def days_left(self):
        if self.is_active():
            return (self.active_until - timezone.now().date()).days
        return 0

    def extend_subscription(self, duration_days=30):
        if self.is_active():
            self.active_until += timedelta(days=duration_days)
        else:
            self.active_until = timezone.now().date() + timedelta(days=duration_days)
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.type} Subscription"
