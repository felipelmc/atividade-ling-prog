from django.contrib import admin
from django.urls import path
from viniapp import views as vini_views

urlpatterns = [
    path('', vini_views.index, name="vini url"),
    path('redes_sociais', vini_views.redes_sociais, name="vini2 url"),
    path('musicas', vini_views.musicas, name="vini3 url"),
]