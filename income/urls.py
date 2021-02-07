from django.urls import path
from .views import IncomeList, IncomeDetailView, TotalIncome


urlpatterns = [
    path('', IncomeList.as_view()),
    path('<int:id>', IncomeDetailView.as_view()),
    path('total/', TotalIncome.as_view()),

]
