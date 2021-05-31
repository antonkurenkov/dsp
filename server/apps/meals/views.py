from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Meal, DailyEat, Ingredient, Schedule


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name", "description", "category", "vegan", "calories", "units"]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["name", "recipe", "ingredients", "description", "time_to_cook"]


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["user"]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]


class DailyEatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyEat
        fields = ["schedule", "meals", "time"]


class DailyEatViewSet(viewsets.ModelViewSet):
    queryset = DailyEat.objects.all()
    serializer_class = DailyEatSerializer
    permission_classes = [IsAuthenticated]
