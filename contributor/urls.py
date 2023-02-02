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
    path('menu', views.menu, name="menu"),
    path('app-menus', csrf_exempt(views.app_menus),
         name="app-menus"),
    path('menu_add', csrf_exempt(views.menu_add),
         name="menu_add"),
]
