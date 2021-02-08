from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense, MainCategory, SubCategory, ModeOfPayment

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields = ['id', 'amount', 'main_category', 'sub_category', 'description',
                  'mode_of_payment', 'date', 'time'
                  ]

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields= ['main_category']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields= ['char','sub_category']

class ModeOfPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeOfPayment
        fields= ['mode_of_payment']
