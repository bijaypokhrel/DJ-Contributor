from django.shortcuts import render, redirect
from .models import Claim_Booking
import json
from django.http import JsonResponse
import datetime


# Create your views here.


def menu(request):
    return render(request, 'menu.html')


def app_menus(request):
    return JsonResponse([{}, {}], safe=False)


def menu_add(request):
    return render(request, 'menu_add.html')
