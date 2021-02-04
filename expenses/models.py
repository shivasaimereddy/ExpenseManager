from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Expense(models.Model):
    amount = models.FloatField()
    main_category = models.CharField(max_length=266)
    sub_category = models.CharField(max_length=266)
    description = models.TextField()
    mode_of_payment = models.CharField(max_length=266)
    date = models.DateField(default=now)
    time = models.TimeField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.main_category

    class Meta:
         ordering: ['-date']

