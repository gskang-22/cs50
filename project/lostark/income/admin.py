from django.contrib import admin
from .models import Income, Source

# customize admin website
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('owner', 'amount', 'source', 'description', 'date')
    search_field = ('owner', 'amount', 'source', 'description', 'date')

# Register your models here.

admin.site.register(Income, IncomeAdmin)
admin.site.register(Source)
