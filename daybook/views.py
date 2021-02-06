from daybook.serializers import incomeserializer, expenseserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required 
from rest_framework.permissions import IsAuthenticated
from expenses.models import Expense
from income.models import Income
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView

from django.db.models import Sum



class daybook(ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request):
        income = Income.objects.filter(owner=request.user)
        expenses = Expense.objects.filter(owner=request.user)
        inc = incomeserializer(income, many=True)
        exp = expenseserializer(expenses, many=True)
        inc_sum = income.aggregate(Sum('amount'))['amount__sum']
        exp_sum = expenses.aggregate(Sum('amount'))['amount__sum']
        balance = inc_sum - exp_sum
        Resultmodel = inc.data+exp.data
        Daybook = ({'Total Income': inc_sum if inc_sum else 0 ,
                    'Total Expenses': exp_sum if exp_sum else 0, 
                    'Balance' : balance if balance else 0,
                    'Daybook': Resultmodel})
        return Response(Daybook)

    def get_queryset(self):
        return Daybook.objects.filter(owner=self.request.user)




