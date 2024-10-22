# nutrition_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.nutrition_category_list, name='nutrition_category_list'),
    path('categories/<int:pk>/', views.nutrition_category_detail, name='nutrition_category_detail'),
    path('nutrition', views.nutrition_list, name='nutrition_list'),
    path('nutrition/<int:pk>/', views.nutrition_detail, name='nutrition_detail'),
]
