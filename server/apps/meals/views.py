from rest_framework import serializers, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Meal, DailyEat, Ingredient, Schedule
from .pagination import ReactAdminPagination


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "description", "category", "vegan", "calories", "units"]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [AllowAny]
    pagination_class = ReactAdminPagination


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "name", "recipe", "ingredients", "description", "time_to_cook"]


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [AllowAny]
    pagination_class = ReactAdminPagination


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["id", "user"]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [AllowAny]
    pagination_class = ReactAdminPagination


class DailyEatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyEat
        fields = ["id", "schedule", "meals", "time"]


class DailyEatViewSet(viewsets.ModelViewSet):
    queryset = DailyEat.objects.all()
    serializer_class = DailyEatSerializer
    permission_classes = [AllowAny]
    pagination_class = ReactAdminPagination
