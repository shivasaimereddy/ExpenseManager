from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Income, SourceOfIncome, ReceivedSource

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'amount', 'source_of_income', 'description', 'received_source', 'date', 'time']

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceOfIncome
        fields = ['source_of_income']

class ReceivedSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedSource
        fields = ['received_source']



