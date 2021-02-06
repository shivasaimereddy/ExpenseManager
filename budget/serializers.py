from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['total_income', 'total_expense', 'balance']