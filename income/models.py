from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class SourceOfIncome(models.Model):
    source_of_income = models.CharField(max_length=226)

    def __str__(self):
        return self.source_of_income


class ReceivedSource(models.Model):
    received_source = models.CharField(max_length=226)

    def __str__(self):
        return self.received_source


class Income(models.Model):
    amount = models.FloatField()
    source_of_income = models.ForeignKey(SourceOfIncome, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    received_source = models.ForeignKey(ReceivedSource, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=now)
    time = models.TimeField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.description

    class Meta:
        ordering: ['-date']



    






