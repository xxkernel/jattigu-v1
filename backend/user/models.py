from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone
from datetime import timedelta

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined =  models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(null=True, blank=True)
    subscription = models.ForeignKey('Subscription', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_subscription')
    current_training_plan = models.ForeignKey('exercise.TrainingPlan', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_current_training_plan')
    favorite = models.ManyToManyField('exercise.Exercise',blank=True, related_name='favorite')
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True)

    # Атрибуты для фитнес-целей
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fitness_goal = models.CharField(max_length=50, choices=[('Lose Weight', 'Lose Weight'), ('Build Muscle', 'Build Muscle'), ('Stay Fit', 'Stay Fit')], blank=True)

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

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["first_name", "last_name"]
    REQUIRED_FIELDS = ["first_name", "last_name", "age", "gender", "weight", "height", "fitness_goal"]

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