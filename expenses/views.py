from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework import permissions
from accounts.views import LoginAPI
from knox.models import AuthToken
from rest_framework.authentication import TokenAuthentication
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response


class ExpenseList(ListCreateAPIView):

    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request):
        expenses = Expense.objects.filter(owner=request.user)
        serializer = ExpenseSerializer(expenses, many=True)
        total_expenses = expenses.aggregate(Sum('amount'))['amount__sum']
        ExpenseTable = ({'Total Expenses': total_expenses if total_expenses else 0 , 'Expenses': serializer.data})
        return Response(ExpenseTable)

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
        

class ExpenseDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
    
   
class TotalExpenses(ListAPIView):

    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get(self, request):
        expenses = Expense.objects.filter(owner=request.user)
        serializer = ExpenseSerializer(expenses, many=True)
        total_expenses = expenses.aggregate(Sum('amount'))['amount__sum']
        ExpenseTable = ({'Total Expenses': total_expenses if total_expenses else 0})
        return Response(ExpenseTable)

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)

    
    
