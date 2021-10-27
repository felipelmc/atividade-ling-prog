from django.urls import path
from sofiaapp import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),