# expenses/models.py

from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Expense(models.Model):
    EQUAL = 'equal'
    EXACT = 'exact'
    PERCENTAGE = 'percentage'
    
    SPLIT_CHOICES = [
        (EQUAL, 'Equal'),
        (EXACT, 'Exact'),
        (PERCENTAGE, 'Percentage')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    split_method = models.CharField(max_length=10, choices=SPLIT_CHOICES)

    def __str__(self):
        return f"{self.description} - {self.amount}"
