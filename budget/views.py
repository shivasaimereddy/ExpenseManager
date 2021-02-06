from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BudgetSerializer
from .models import Budget
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required 
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from expenses.models import Expense
from income.models import Income


# Create your views here.


@api_view(['GET']) 
#@login_required(login_url='/api/login')  
@permission_classes([IsAuthenticated])
def budget(request):
    income = Income.objects.filter(owner = request.user)
    expense = Expense.objects.filter(owner = request.user)


    budget = Budget.objects.filter(owner=request.user)
    budgetser = BudgetSerializer(budget, many=True)
    Resultmodel = budgetser.data
    return Response(Resultmodel)