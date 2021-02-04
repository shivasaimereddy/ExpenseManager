from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields = ['id', 'amount', 'main_category', 'sub_category', 'description',
                  'mode_of_payment', 'date', 'time'
                  ]
