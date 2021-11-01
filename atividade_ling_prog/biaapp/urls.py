from django.urls import path
from django.urls.conf import include
from biaapp import views as biaapp_views 

urlpatterns = [
    path('', biaapp_views.index, name='teste'),
    path('biaapp/', biaapp_views.bia, name='biaapp'),
    path('pag1/', biaapp_views.pag1, name='pag1'),
    path('pag2/', biaapp_views.pag2, name='pag2'),
]