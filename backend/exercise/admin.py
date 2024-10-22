from django.contrib import admin
from .models import Exercise, ExerciseLevel, ExerciseCategory, ExerciseEquipment, TrainingPlan, TrainingPlanExercise, Schedule

@admin.register(ExerciseLevel)
class ExerciseLevelAdmin(admin.ModelAdmin):
    list_display = ('level_name',)
    search_fields = ('level_name',)

@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

@admin.register(ExerciseEquipment)
class ExerciseEquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment_name',)
    search_fields = ('equipment_name',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'intensity', 'calories', 'image')
    search_fields = ('name', 'description')
    list_filter = ('intensity', 'category', 'level', 'equipment')

@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_in_weeks', 'goal', 'level')
    search_fields = ('name', 'description')
    list_filter = ('level',)

@admin.register(TrainingPlanExercise)
class TrainingPlanExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'sets', 'reps', 'rest_period', 'day')
    search_fields = ('exercise__name',)
    list_filter = ('exercise',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('training_plan', 'date', 'completed')
    list_filter = ('completed',)
    search_fields = ('training_plan__name',)
