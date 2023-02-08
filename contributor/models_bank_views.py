from django.shortcuts import render, redirect
# from .models import Claim_Booking
import json
from django.http import JsonResponse
import datetime
from .models_bank import Bank


# Create your views here.


def bank(request):
    return render(request, 'bank.html')


def app_banks(request, bank_id=None):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        capital = data.get('capital')
        bank = Bank(name=name, capital=capital)
        bank.save()
    # return JsonResponse([{}, {}], safe=False)

    if request.method == "PUT":
        data = json.loads(request.body)
        bank = Bank.objects.filter(pk=bank_id).first()
        bank.name = data.get('name')
        bank.capital = data.get('capital')
        # menu = Menu(menu_text=menu_text, menu_link=menu_link)
        bank.save()

    if request.method == "DELETE":
        bank = Bank.objects.filter(pk=bank_id).first()
        bank.delete()
    banks = []
    for bank in Bank.objects.all():
        banks.append({
            'id': bank.pk,
            'name': bank.name,
            'capital': bank.capital,
        })
    return JsonResponse(banks, safe=False)


def bank_add(request):
    return render(request, 'bank_add.html')


def bank_edit(request):
    return render(request, 'bank_edit.html')


# def bank_edit_api(request):
#     return render(request, 'bank_edit_api.html')


def bank_delete(request):
    return render(request, 'bank_delete.html')


def bank_graphql(request):
    return render(request, 'bank_graphql.html')
