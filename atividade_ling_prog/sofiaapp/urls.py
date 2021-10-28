from django.urls import path
from sofiaapp import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('sofiaapp/', views.sofia, name='sofiaapp'),
]