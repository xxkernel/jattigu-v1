from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('NutritionCategory', on_delete=models.CASCADE, related_name='food_items')
    # Дополнительные атрибуты для модели FoodItem
    description = models.TextField(blank=True, help_text="Описание продукта")

    def __str__(self):
        return self.name

class NutritionCategory(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    # Дополнительные атрибуты
    description = models.TextField(blank=True, help_text="Описание категории питания")
    popularity_score = models.IntegerField(default=0, help_text="Популярность категории, используется для сортировки")

    def get_all_subcategories(self):
        """Возвращает все подкатегории, связанные с данной категорией."""
        return self.subcategories.all()

    def has_subcategories(self):
        """Проверяет, есть ли у категории подкатегории."""
        return self.subcategories.exists()

    def total_food_items(self):
        """Возвращает общее количество продуктов в данной категории и ее подкатегориях."""
        total_items = FoodItem.objects.filter(category=self).count()
        for subcategory in self.subcategories.all():
            total_items += subcategory.total_food_items()
        return total_items

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField(help_text="Количество калорий на порцию")
    macronutrients = models.JSONField(
        help_text="Макроэлементы в формате JSON (например, {'protein': 10, 'fat': 5, 'carbohydrates': 20})")
    category = models.ForeignKey('NutritionCategory', on_delete=models.CASCADE, related_name='nutritional_items')

    # Дополнительные атрибуты
    serving_size = models.CharField(max_length=50, help_text="Размер порции, например, '100g' или '1 cup'")
    is_vegan = models.BooleanField(default=False, help_text="Флаг, указывающий, является ли продукт веганским")
    is_gluten_free = models.BooleanField(default=False,
                                         help_text="Флаг, указывающий, является ли продукт безглютеновым")
    allergens = models.CharField(max_length=255, blank=True,
                                 help_text="Список аллергенов, если есть (например, 'орехи, молоко')")

    def get_macronutrient(self, nutrient):
        """Возвращает значение указанного макроэлемента, если он присутствует."""
        return self.macronutrients.get(nutrient, 0)

    def total_calories_per_serving(self):
        """Возвращает общее количество калорий на порцию."""
        return self.calories

    def __str__(self):
        return self.name
