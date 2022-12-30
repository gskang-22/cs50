from django.contrib import admin
from .models import Expense, Category


# customize admin website
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('owner', 'amount', 'category', 'description', 'date')
    search_fields = ('description', 'category', 'date')

    list_per_page = 5


# Register your models here.

admin.site.register(Expense, ExpenseAdmi)
admin.site.register(Category)