from django.contrib import admin
from .models import Budget

# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('Total_Income', 'Total_Expenses', 'Balance')

admin.site.register(Budget, BudgetAdmin)

