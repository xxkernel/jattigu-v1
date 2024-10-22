from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            'id', 
            'email', 
            'first_name', 
            'last_name', 
            'password',
            'age', 
            'gender', 
            'weight', 
            'height', 
            'fitness_goal'
            # Исключаем 'subscription', 'current_training_plan' и 'favorite'
        ]
