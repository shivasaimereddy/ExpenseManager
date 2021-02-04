from django.contrib import admin
from .models import Income

# Register your models here.

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id','amount', 'source_of_income','description','received_source','owner', 'date', 'time')


admin.site.register(Income, IncomeAdmin)

