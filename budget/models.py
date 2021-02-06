from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Budget(models.Model):
    total_income = models.FloatField()
    total_expense = models.FloatField()
    balance = models.FloatField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


