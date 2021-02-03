from django.contrib import admin
from .models import Income, Source

# Register your models here.

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id','amount', 'source_of_income','description','received_source','owner', 'date')


admin.site.register(Income, IncomeAdmin)
admin.site.register(Source)

