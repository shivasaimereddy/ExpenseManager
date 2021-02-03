from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Income
from .serializers import IncomeSerializer
from rest_framework import permissions


class IncomeList(ListCreateAPIView):

    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)


class IncomeDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)