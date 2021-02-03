from django.urls import path
from .views import IncomeList, IncomeDetailView


urlpatterns = [
    path('', IncomeList.as_view()),
    path('<int:id>', IncomeDetailView.as_view()),
]