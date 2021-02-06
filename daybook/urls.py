from django.urls import path
from . import views
from .views import daybook


urlpatterns = [
    path('', daybook.as_view()),
]
