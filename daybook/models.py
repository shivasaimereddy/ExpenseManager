from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Budget(models.Model):
    Total_Income = models.FloatField()
    Total_Expenses = models.FloatField()
    Balance = models.FloatField()


