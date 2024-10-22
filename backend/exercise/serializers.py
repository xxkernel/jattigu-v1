# serializers.py
from rest_framework import serializers
from .models import Exercise, ExerciseCategory, ExerciseEquipment, ExerciseLevel, TrainingPlan, TrainingPlanExercise, Schedule

class ExerciseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCategory
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'  # Вы можете указать конкретные поля, если это необходимо

class TrainingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPlan
        fields = '__all__'

class TrainingPlanExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPlanExercise
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ExerciseLevelSerializer(serializers.ModelSerializer):  # Create the serializer for ExerciseLevel
    class Meta:
        model = ExerciseLevel
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):  # Create the serializer for Equipment
    class Meta:
        model = ExerciseEquipment
        fields = '__all__'