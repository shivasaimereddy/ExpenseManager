from rest_framework import serializers
from expenses.models import Expense
from income.models import Income

class expenseserializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields=['id', 'amount', 'main_category', 'sub_category', 'description', 'mode_of_payment', 'date']


class incomeserializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'amount', 'source_of_income', 'description', 'received_source', 'date']
    