from django.shortcuts import render, get_object_or_404
from .models import Exercise, TrainingPlan, ExerciseCategory, ExerciseLevel


def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_management/exercise_list.html', {'exercises': exercises})


def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'exercise_management/exercise_detail.html', {'exercise': exercise})


def training_plan_list(request):
    training_plans = TrainingPlan.objects.all()
    return render(request, 'exercise_management/training_plan_list.html', {'training_plans': training_plans})


def training_plan_detail(request, pk):
    training_plan = get_object_or_404(TrainingPlan, pk=pk)
    return render(request, 'exercise_management/training_plan_detail.html', {'training_plan': training_plan})


def schedule_list(request):
    training_plans = TrainingPlan.objects.all()
    return render(request, 'exercise_management/schedule_list.html', {'training_plans': training_plans})
