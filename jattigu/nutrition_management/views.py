from django.shortcuts import render, get_object_or_404
from .models import NutritionCategory, FoodItem, Nutrition

# Список категорий питания
def nutrition_category_list(request):
    categories = NutritionCategory.objects.all()
    return render(request, 'nutrition_management/nutrition_category_list.html', {'categories': categories})

# Детали категории питания
def nutrition_category_detail(request, pk):
    category = get_object_or_404(NutritionCategory, pk=pk)
    return render(request, 'nutrition_management/nutrition_category_detail.html', {'category': category})

# Список продуктов питания
def nutrition_list(request):
    nutritional_items = Nutrition.objects.all()
    return render(request, 'nutrition_management/nutrition_list.html', {'nutritional_items': nutritional_items})

# Детали продукта питания
def nutrition_detail(request, pk):
    nutrition_item = get_object_or_404(Nutrition, pk=pk)
    return render(request, 'nutrition_management/nutrition_detail.html', {'nutrition_item': nutrition_item})


