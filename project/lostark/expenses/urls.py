from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expenses', views.add_expense, name="add-expenses"),
    path('edit-expenses/<int:id>', views.edit_expense, name="edit-expenses"),
    path('delete-expenses/<int:id>', views.delete_expense, name="delete-expenses"),
    path('search-expenses', csrf_exempt(views.search_expenses), name="search-expenses"),
    path('expense-category-summary', views.expense_category_summary, name=expense-category-summary),
    path('stats-view', views.stats_view, name='stats-view')
]