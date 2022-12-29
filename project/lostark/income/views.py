from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Source, Income
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
import json

# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    income = Income.objects.filter(owner=request.user)
    paginator = Paginator(income, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'income': income,
        'page_obj': page_obj
    }
    return render(request, 'income/index.html', context)


def add_income(request):
    source = Source.objects.all()
    context = {
            'source': source,
            'values': request.POST
        }
    if request.method == "GET":
        return render(request, 'income/add_income.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/add_income.html', context)

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'income/add_income.html', context)

        if not date:
            Income.objects.create(owner=request.user, amount=amount, source=source, description=description)
        else:
            Income.objects.create(owner=request.user, amount=amount, date=date, source=source, description=description)

        messages.success(request, 'Income saved successfully')
        return redirect('income')


def edit_income(request, id):
    income = Income.objects.get(pk=id)
    source = Source.objects.all()

    context = {
        'income': income,
        'values': values,
        'source': source
    }
    if request.method == 'GET':
        return render(request, 'income/edit_income.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/edit_income.html', context)

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'income/edit_income.html', context)

        income.owner = request.user
        income.amount = amount
        income.source = source
        income.description = description
        if date:
            income.date = date

        income.save()
        messages.success(request, 'Income updated successfully')
        return redirect('income')


def delete_income(request, id):
    income = Income.objects.get(pk=id)
    income.delete()
    messages.success(request, 'Income deleted')
    return redirect('income')


def search_income(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        income = Income.objects.filter(
            amount__istartswith=search_str, owner=request.user) | Income.objects.filter(
            date__istartswith=search_str, owner=request.user) | Income.objects.filter(
            description__icontains=search_str, owner=request.user) | Income.objects.filter(
            source__icontains=search_str, owner=request.user)

        data = income.values()
        # change to list as it is difficult to work with a query set
        return JsonResponse(list(data), safe=False)