from django.db import models
from budget.models import Budget
# Create your models here.
class ShoppingList(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    description = models.TextField()