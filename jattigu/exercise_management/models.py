from django.db import models


class Exercise(models.Model):
    # Основная информация
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Время выполнения в минутах
    duration = models.IntegerField(help_text="Duration in minutes")

    # Интенсивность упражнения (низкая, средняя, высокая)
    intensity = models.CharField(max_length=50, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ])

    # Категории упражнений (например, кардио, силовые)
    category = models.ManyToManyField('ExerciseCategory', related_name='exercises')

    # Уровень сложности упражнения
    level = models.ForeignKey('ExerciseLevel', on_delete=models.CASCADE, related_name='exercises')

    # Дополнительные атрибуты
    equipment_needed = models.CharField(max_length=100, blank=True,
                                        help_text="Equipment required (e.g., Dumbbells, Resistance Band)")
    calories_burned_per_minute = models.DecimalField(max_digits=5, decimal_places=2,
                                                     help_text="Estimated calories burned per minute")
    muscle_groups = models.CharField(max_length=200, help_text="Target muscle groups (e.g., arms, legs, core)")

    def total_calories_burned(self):
        """Расчет общего количества калорий, сожжённых за время выполнения упражнения"""
        return self.duration * self.calories_burned_per_minute

    def is_high_intensity(self):
        """Проверяет, является ли упражнение высокоинтенсивным"""
        return self.intensity == 'High'

    def __str__(self):
        return f"{self.name} - {self.level.level_name} Level"

class ExerciseLevel(models.Model):
    level_name = models.CharField(max_length=50)  # Например, Beginner, Normal, Hard

    def exercise_count(self):
        """Возвращает количество упражнений для данного уровня сложности."""
        return self.exercises.count()

    def total_duration(self):
        """Возвращает общую длительность всех упражнений данного уровня сложности в минутах."""
        return sum(exercise.duration for exercise in self.exercises.all())

    def average_calories_burned(self):
        """Возвращает среднее количество калорий, сожжённых за одно упражнение данного уровня."""
        exercises = self.exercises.all()
        if exercises:
            total_calories = sum(exercise.total_calories_burned() for exercise in exercises)
            return total_calories / exercises.count()
        return 0

    def __str__(self):
        return self.level_name


class ExerciseCategory(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                        related_name='subcategories')

    # Дополнительные атрибуты
    description = models.TextField(blank=True, help_text="Описание категории упражнений")
    popularity_score = models.IntegerField(default=0, help_text="Популярность категории, используется для сортировки")

    def get_all_exercises(self):
        """Возвращает все упражнения, относящиеся к данной категории, включая подкатегории."""
        exercises = list(self.exercises.all())
        for subcategory in self.subcategories.all():
            exercises.extend(subcategory.get_all_exercises())
        return exercises

    def has_subcategories(self):
        """Проверяет, есть ли у категории подкатегории."""
        return self.subcategories.exists()

    def total_exercise_count(self):
        """Возвращает общее количество упражнений, включая упражнения в подкатегориях."""
        return len(self.get_all_exercises())

    def __str__(self):
        return self.name

class TrainingPlan(models.Model):
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField('Exercise', through='TrainingPlanExercise', related_name='training_plans')

    # Дополнительные атрибуты
    description = models.TextField(blank=True, help_text="Описание плана тренировки")
    level = models.ForeignKey('ExerciseLevel', on_delete=models.SET_NULL, null=True, blank=True, help_text="Рекомендуемый уровень для этого плана")
    duration_in_weeks = models.PositiveIntegerField(help_text="Длительность плана в неделях")
    goal = models.CharField(max_length=100, help_text="Основная цель плана (например, потеря веса, набор мышц)")

    def total_exercise_duration(self):
        """Возвращает общую длительность всех упражнений в плане тренировки (в минутах)."""
        return sum(relation.exercise.duration for relation in self.trainingplanexercise_set.all())

    def total_calories_burned(self):
        """Возвращает общее количество калорий, сожженных за выполнение всех упражнений в плане."""
        return sum(relation.exercise.total_calories_burned() for relation in self.trainingplanexercise_set.all())

    def exercise_count(self):
        """Возвращает количество упражнений в плане тренировки."""
        return self.exercises.count()

    def get_exercises_by_day(self, day):
        """Возвращает упражнения, запланированные на указанный день."""
        return self.trainingplanexercise_set.filter(day=day).values_list('exercise', flat=True)

    def __str__(self):
        return self.name


class TrainingPlanExercise(models.Model):
    training_plan = models.ForeignKey('TrainingPlan', on_delete=models.CASCADE, related_name='plan_exercises')
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='exercise_plans')

    # Основные параметры выполнения упражнения
    sets = models.IntegerField(help_text="Количество подходов")
    reps = models.IntegerField(help_text="Количество повторений в подходе")

    # Дополнительные атрибуты
    rest_period = models.IntegerField(default=60, help_text="Время отдыха между подходами в секундах")
    day = models.PositiveIntegerField(null=True, blank=True,
                                      help_text="День недели или дня плана для выполнения упражнения")
    notes = models.TextField(blank=True, help_text="Дополнительные заметки для выполнения упражнения")

    def total_reps(self):
        """Возвращает общее количество повторений для данного упражнения в плане."""
        return self.sets * self.reps

    def total_exercise_duration(self):
        """Возвращает общую продолжительность выполнения упражнения с учетом отдыха (в минутах)."""
        exercise_duration = self.exercise.duration * self.sets
        total_rest_time = (self.sets - 1) * self.rest_period  # Время отдыха между подходами
        total_duration = exercise_duration + total_rest_time / 60
        return total_duration

    def is_high_intensity(self):
        """Проверяет, является ли упражнение высокоинтенсивным в зависимости от количества повторений и подходов."""
        return self.sets >= 4 and self.reps >= 15

    def __str__(self):
        return f"{self.exercise.name} in {self.training_plan.name} - {self.sets} sets of {self.reps} reps"


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
