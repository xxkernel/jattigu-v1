# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog_post_list, name='blog_post_list'),
    path('blog/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('categories/', views.blog_category_list, name='blog_category_list'),
    path('categories/<int:pk>/', views.blog_category_detail, name='blog_category_detail'),
]
