from django.urls import path, include
from .views import users
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('', viewset = views.UserListViewSet)

urlpatterns = [
    path('', include(router.urls))
]