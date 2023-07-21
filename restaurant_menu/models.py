from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('appetites', 'Appetites'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts'),
)

AVAILABILITY = (
    (0, 'Unavailable'),
    (1, 'Available'),
)


# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    ingredients = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200, choices=CATEGORY)
    # Cascade means when the author is deleted, all his dishes are also deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    availability = models.IntegerField(choices=AVAILABILITY, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
