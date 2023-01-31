from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('claimbooking', views.claim_booking, name="claimbooking"),
    path('claimbookingjson', csrf_exempt(views.claim_booking_json),
         name="claimbookingjson"),
    # path('claimbookingfhir', csrf_exempt(views.claim_booking_fhir),
    #      name="claimbookingfhir"),
]
