from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('claimbooking', views.claim_booking, name="claimbooking"),
    path('claimbookingjson', csrf_exempt(views.claim_booking_json),
         name="claimbookingjson"),
    path('claimbookingfhir', csrf_exempt(views.claim_booking_fhir),
         name="claimbookingfhir"),
    path('fhirbookingclaim/<int:claim_id>', csrf_exempt(views.get_claim),
         name="fhirbookingclaim"),

    # Menu
    path('menu', views.menu, name="menu"),
    path('app-menus', csrf_exempt(views.app_menus),
         name="app-menus"),
    path('app_menus/<int:menu_id>', csrf_exempt(views.app_menus)),
    path('menu_add', csrf_exempt(views.menu_add),
         name="menu_add"),
    path('menu_edit', csrf_exempt(views.menu_edit),
         name="menu_edit"),
    path('menu_delete', csrf_exempt(views.menu_delete),
         name="menu_delete"),

    # Bank
    path('bank', views.bank, name="bank"),
    path('app-banks', csrf_exempt(views.app_banks),
         name="app-banks"),
    path('app-banks/<int:bank_id>', csrf_exempt(views.app_banks)),
    path('bank_add', csrf_exempt(views.bank_add),
         name="bank_add"),
    path('bank_edit', csrf_exempt(views.bank_edit),
         name="bank_edit"),
    path('bank_delete', csrf_exempt(views.bank_delete),
         name="bank_delete"),

]
