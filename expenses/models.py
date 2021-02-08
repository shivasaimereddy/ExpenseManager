from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class MainCategory(models.Model):
    main_category = models.CharField(max_length=266)

    def __str__(self):
        return self.main_category

class SubCategory(models.Model):
    sub_category = models.CharField(max_length=266)

    def __str__(self):
        return self.sub_category

class ModeOfPayment(models.Model):
    mode_of_payment = models.CharField(max_length=266)

    def __str__(self):
        return self.mode_of_payment


class Expense(models.Model):
    amount = models.FloatField()
    main_category = models.ForeignKey(MainCategory, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    mode_of_payment = models.ForeignKey(ModeOfPayment, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=now)
    time = models.TimeField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.main_category

    class Meta:
         ordering: ['-date']





