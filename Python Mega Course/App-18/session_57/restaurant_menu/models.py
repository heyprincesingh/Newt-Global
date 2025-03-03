from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore


MEAL_TYPES = (
    ('starter', 'Starter'),
    ('salad', 'Salad'),
    ('main_dishes', 'Main Dishes'),
    ('dessert', 'Dessert')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
