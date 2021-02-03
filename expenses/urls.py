from django.urls import path
from .views import ExpenseList, ExpenseDetailView


urlpatterns = [
    path('', ExpenseList.as_view()),
    path('<int:id>', ExpenseDetailView.as_view()),
]