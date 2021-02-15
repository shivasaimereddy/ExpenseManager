from django.urls import path, include
from .views import users
from . import views

urlpatterns = [
    path('', users.as_view()),
]