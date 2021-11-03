from django.urls import path
from django.urls.conf import include
from felipeapp import views as felipeapp_views 

urlpatterns = [
    path('', felipeapp_views.index, name='teste'),
    path('redes-sociais/', felipeapp_views.pag1, name='felipeapp'),
    path('musicas/', felipeapp_views.pag2, name='felipeapp'),
    path('faculdade/', felipeapp_views.pag3, name='felipeapp'),
]

