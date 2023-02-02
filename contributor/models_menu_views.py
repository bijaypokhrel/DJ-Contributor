from django.shortcuts import render, redirect
from .models import Claim_Booking
import json
from django.http import JsonResponse
import datetime
from .models_menu import Menu


# Create your views here.


def menu(request):
    return render(request, 'menu.html')


def app_menus(request):
    if request.method == "POST":
        data = json.loads(request.body)
        menu_text = data.get('menu_text')
        menu_link = data.get('menu_link')
        menu = Menu(menu_text=menu_text, menu_link=menu_link)
        menu.save()
    # return JsonResponse([{}, {}], safe=False)
    menus = []
    for menu in Menu.objects.all():
        menus.append({
            'menu_text': menu.menu_text,
            'menu_link': menu.menu_link,
        })
    return JsonResponse(menus, safe=False)


def menu_add(request):
    return render(request, 'menu_add.html')
