from daybook.serializers import incomeserializer, expenseserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required 
from rest_framework.permissions import IsAuthenticated
from expenses.models import Expense
from income.models import Income
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
    


@api_view(['GET']) 
#@login_required(login_url='/api/login')  needed to redirect user to login page whe unauthorized
@permission_classes([IsAuthenticated])
def daybook(request):
    incobj = Income.objects.all()
    expobj = Expense.objects.all()
    inserobj = incomeserializer(incobj, many=True)
    expserobj = expenseserializer(expobj, many=True)
    Resultmodel = inserobj.data+expserobj.data
    return Response(Resultmodel)
   

