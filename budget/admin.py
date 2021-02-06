from django.contrib import admin
from .models import Budget

# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('total_income', 'total_expense', 'balance', 'owner')

admin.site.register(Budget, BudgetAdmin)
