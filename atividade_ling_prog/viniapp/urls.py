from django.contrib import admin
from django.urls import path
from viniapp import views as vini_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vini_views.index, name="vini url")
]