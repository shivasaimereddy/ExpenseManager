from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView ,ListAPIView
from .models import Income
from .serializers import IncomeSerializer
from rest_framework import permissions
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response



class IncomeList(ListCreateAPIView):

    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request):
        income = Income.objects.filter(owner=request.user)
        serializer = IncomeSerializer(income, many=True)
        total_income = income.aggregate(Sum('amount'))['amount__sum']
        IncomeTable = ({'Total Income': total_income if total_income else 0 , 'Income': serializer.data})
        return Response(IncomeTable)

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)



class IncomeDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)
    
    
    
class TotalIncome(ListAPIView):

    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)  

    def get(self, request):
        income = Income.objects.filter(owner=request.user)
        serializer = IncomeSerializer(income, many=True)
        total_income = income.aggregate(Sum('amount'))['amount__sum']
        IncomeTable = ({'Total Income': total_income if total_income else 0})
        return Response(IncomeTable)

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)


         




