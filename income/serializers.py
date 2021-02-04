from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Income

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'amount', 'source_of_income', 'description', 'received_source', 'date', 'time']

