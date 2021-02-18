from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required 
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import authentication, permissions


from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView

from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import mixins


# Create your views here.
"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):
    user = User.objects.all()
    ser= UserSerializer(user, many=True)
    Result = ser.data
    return Response(Result)
    """

class users(ListAPIView):

    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        user = User.objects.all()
        ser= UserSerializer(user, many=True)
        Result = ser.data
        return Response(Result)

    def get_queryset(self):
        return User.objects.filter(username = self.request.user)


class UserListViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


