from django.shortcuts import render, redirect
# from .models import Claim_Booking
import json
from django.http import JsonResponse
import datetime
from .models_menu import Menu


# Create your views here.


def menu(request):
    return render(request, 'menu.html')


def app_menus(request, menu_id=None):
    if request.method == "POST":
        data = json.loads(request.body)
        menu_text = data.get('menu_text')
        menu_link = data.get('menu_link')
        menu = Menu(menu_text=menu_text, menu_link=menu_link)
        menu.save()
    # return JsonResponse([{}, {}], safe=False)
    if request.method == "PUT":
        data = json.loads(request.body)
        menu = Menu.objects.filter(pk=menu_id).first()
        menu.menu_text = data.get('menu_text')
        menu.menu_link = data.get('menu_link')
        # menu = Menu(menu_text=menu_text, menu_link=menu_link)
        menu.save()

    if request.method == "DELETE":
        menu = Menu.objects.filter(pk=menu_id).first()
        menu.delete()
    menus = []
    for menu in Menu.objects.all():
        menus.append({
            'id': menu.pk,
            'menu_text': menu.menu_text,
            'menu_link': menu.menu_link,
        })
    return JsonResponse(menus, safe=False)


def menu_add(request):
    return render(request, 'menu/menu_add.html')


def menu_edit(request):
    return render(request, 'menu/menu_edit.html')


def menu_delete(request):
    return render(request, 'menu/menu_delete.html')


def menu_list(request):
    return render(request, 'menu/menu_list.html')


def menu_list_edit(request):
    return render(request, 'menu/menu_list_edit.html')
