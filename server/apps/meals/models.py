from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    UNITS = (
        ("g", "g"),
        ("ml", "ml"),
        ("pcs", "pcs"),
    )
    CATEGORIES = (
        ("milk", "milk"),
        ("cereal", "cereal"),
        ("meat", "meat"),
        ("green", "green"),
        ("bread", "bread"),
        ("grocery", "grocery"),
        ("spices", "spices"),
        ("drinks", "drinks"),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, null=True)
    vegan = models.BooleanField(null=True)
    calories = models.IntegerField(null=True)
    units = models.CharField(max_length=50, choices=UNITS, null=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.JSONField(null=True)
    ingredients = models.ManyToManyField(to=Ingredient, related_name="meals")
    description = models.TextField(null=True)
    time_to_cook = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}'s Schedule"


class DailyEat(models.Model):
    schedule = models.ForeignKey(to=Schedule, on_delete=models.CASCADE, null=True)
    meals = models.ManyToManyField(to=Meal, related_name="daily_eats")
    time = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.schedule.user}'s {self.time} meal"
