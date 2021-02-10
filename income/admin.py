from django.contrib import admin
from .models import Income, SourceOfIncome, ReceivedSource

# Register your models here.

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id','amount', 'source_of_income','description','received_source','owner', 'date', 'time')

class SourceAdmin(admin.ModelAdmin):
    list_display = ['source_of_income']

class ReceivedSourceAdmin(admin.ModelAdmin):
    list_display = ['received_source']



admin.site.register(Income, IncomeAdmin)
#admin.site.register(SourceOfIncome, SourceAdmin)
#admin.site.register(ReceivedSource, ReceivedSourceAdmin)


