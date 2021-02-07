from django.urls import path
from .views import ExpenseList, ExpenseDetailView, TotalExpenses


urlpatterns = [
    path('', ExpenseList.as_view()),
    path('<int:id>', ExpenseDetailView.as_view()),
    path('total/', TotalExpenses.as_view()),

]
