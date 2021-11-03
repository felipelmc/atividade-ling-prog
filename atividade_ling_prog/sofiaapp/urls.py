from django.urls import path
from sofiaapp import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('sofiaapp/', views.sofia, name='sofiaapp'),
    path('laks/', views.laks, name='sofiaapp'),
    path('vitz/', views.vitz, name='sofiaapp'),
]