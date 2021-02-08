from django.contrib import admin
from .models import Expense, MainCategory, SubCategory, ModeOfPayment

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'main_category','sub_category','description','mode_of_payment','owner', 'date', 'time')

class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['main_category']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['char','sub_category']


class ModeOfPaymentAdmin(admin.ModelAdmin):
    list_display = ['mode_of_payment']

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ModeOfPayment, ModeOfPaymentAdmin)


