# exercise_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('exercices', views.exercise_list, name='exercise_list'),
    path('exercice/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('training-plans/', views.training_plan_list, name='training_plan_list'),
    path('training-plans/<int:pk>/', views.training_plan_detail, name='training_plan_detail'),
    path('schedules/', views.schedule_list, name='schedule_list'),
]
