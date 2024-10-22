from django.db import models

class ExerciseLevel(models.Model):
    level_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.level_name
    
class ExerciseCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name

class ExerciseEquipment(models.Model):
    equipment_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.equipment_name


class Exercise(models.Model):  
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")
    intensity = models.CharField(max_length=50, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ])
    category = models.ManyToManyField('ExerciseCategory', related_name='exercises')
    level = models.ForeignKey('ExerciseLevel', on_delete=models.CASCADE, related_name='exercises')
    equipment = models.ManyToManyField('ExerciseEquipment', related_name='exercises')
    calories = models.DecimalField(max_digits=5, decimal_places=2, help_text="Estimated calories burned per minute")
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="URL to the exercise demonstration video")

    def __str__(self):
        return self.name

    

class TrainingPlan(models.Model):
    name = models.CharField(max_length=100)
    training_plan_exercises = models.ForeignKey('TrainingPlan', on_delete=models.CASCADE, related_name='plan_exercises')

    description = models.TextField(blank=True, help_text="Описание плана тренировки")
    level = models.ForeignKey('ExerciseLevel', on_delete=models.SET_NULL, null=True, blank=True, help_text="Рекомендуемый уровень для этого плана")
    duration_in_weeks = models.PositiveIntegerField(help_text="Длительность плана в неделях")
    goal = models.CharField(max_length=100, help_text="Основная цель плана (например, потеря веса, набор мышц)")

    def __str__(self):
        return self.name
    

class TrainingPlanExercise(models.Model):
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='exercise_plans')

    sets = models.IntegerField(help_text="Количество подходов")
    reps = models.IntegerField(help_text="Количество повторений в подходе")

    # Дополнительные атрибуты
    rest_period = models.IntegerField(default=60, help_text="Время отдыха между подходами в секундах")
    day = models.PositiveIntegerField(null=True, blank=True,
                                      help_text="День недели или дня плана для выполнения упражнения")
    notes = models.TextField(blank=True, help_text="Дополнительные заметки для выполнения упражнения")

    def __str__(self):
        return f"{self.exercise.name} in {self.training_plan.name} - {self.sets} sets of {self.reps} reps"
    





# ADDITIONAL

class Schedule(models.Model):
    training_plan = models.ForeignKey('TrainingPlan', on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField(help_text="Дата, на которую запланирована тренировка")

    # Дополнительные атрибуты
    completed = models.BooleanField(default=False, help_text="Флаг выполнения тренировки")
    notes = models.TextField(blank=True, help_text="Заметки о тренировке или прогрессе")
    reminder_time = models.TimeField(null=True, blank=True, help_text="Время напоминания для тренировки")

    def mark_as_completed(self):
        """Отмечает тренировку как выполненную."""
        self.completed = True
        self.save()

    def is_upcoming(self):
        """Проверяет, является ли тренировка предстоящей по дате."""
        from django.utils import timezone
        return self.date >= timezone.now().date()

    def missed_training(self):
        """Проверяет, была ли тренировка пропущена."""
        from django.utils import timezone
        return not self.completed and self.date < timezone.now().date()

    def __str__(self):
        return f"{self.training_plan.name} on {self.date} - {'Completed' if self.completed else 'Pending'}"