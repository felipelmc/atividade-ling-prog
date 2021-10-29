from django.contrib import admin
from django.urls import path
from viniapp import views as vini_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viniapp/', vini_views.vini, name="vini url")
]