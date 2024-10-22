# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    EquipmentListView,
    ExerciseCategoryListView, 
    ExerciseDetailView, 
    ExerciseListView, 
    TrainingPlanListView, 
    TrainingPlanExerciseListView, 
    ScheduleListView,
    ExerciseLevelListView,
    add_exercise  # Import your ExerciseLevelListView
)

urlpatterns = [
    path('', ExerciseListView.as_view(), name='exercise-list'),
    path('<int:id>/', ExerciseDetailView.as_view(), name='exercise-detail'),
    path('training-plans/', TrainingPlanListView.as_view(), name='training-plan-list'),
    path('training-plan-exercises/', TrainingPlanExerciseListView.as_view(), name='training-plan-exercise-list'),
    path('schedules/', ScheduleListView.as_view(), name='schedule-list'),
    path('exercise-categories/', ExerciseCategoryListView.as_view(), name='exercise-category-list'),
    path('exercise-levels/', ExerciseLevelListView.as_view(), name='exercise-level-list'),  # New URL for exercise levels
    path('equipment/', EquipmentListView.as_view(), name='equipment-list'),
    path('add_exercise/', add_exercise, name='add_exercise'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
