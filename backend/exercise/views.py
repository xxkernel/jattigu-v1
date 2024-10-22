# views.py
from requests import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import ExerciseCategory, Exercise, ExerciseEquipment, ExerciseLevel, TrainingPlan, TrainingPlanExercise, Schedule
from .serializers import EquipmentSerializer, ExerciseCategorySerializer, ExerciseLevelSerializer, ExerciseSerializer, TrainingPlanSerializer, TrainingPlanExerciseSerializer, ScheduleSerializer

class ExerciseCategoryListView(generics.ListAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer

class ExerciseDetailView(generics.RetrieveAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    lookup_field = 'id'  # Или вы можете использовать 'pk'
    
class ExerciseListView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class TrainingPlanListView(generics.ListAPIView):
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer

class TrainingPlanExerciseListView(generics.ListAPIView):
    queryset = TrainingPlanExercise.objects.all()
    serializer_class = TrainingPlanExerciseSerializer

class ScheduleListView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ExerciseLevelListView(generics.ListAPIView):  # Create the view for exercise levels
    queryset = ExerciseLevel.objects.all()
    serializer_class = ExerciseLevelSerializer

class EquipmentListView(generics.ListAPIView):  # Create the view for equipment
    queryset = ExerciseEquipment.objects.all()
    serializer_class = EquipmentSerializer


@api_view(['POST'])
def add_exercise(request):
    if request.method == 'POST':
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)