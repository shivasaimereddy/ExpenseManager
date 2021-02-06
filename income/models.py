from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Income(models.Model):
    amount = models.FloatField()
    source_of_income = models.CharField(max_length=266)
    description = models.TextField()
    received_source = models.CharField(max_length=266)
    date = models.DateField(default=now)
    time = models.TimeField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.source_of_income

    class Meta:
        ordering: ['-date']






