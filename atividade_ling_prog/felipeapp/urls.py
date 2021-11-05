from django.urls import path
from django.urls.conf import include
from felipeapp import views as felipeapp_views 

urlpatterns = [
    path('', felipeapp_views.index, name='teste'),
    #path('redes-sociais/', felipeapp_views.pag1, name='felipeapp'),
    #path('musicas/', felipeapp_views.pag2, name='felipeapp'),
    #path('faculdade/', felipeapp_views.pag3, name='felipeapp'),
    path('special_str/<str:param>/', felipeapp_views.view_dinamica_str, name = 'dinamica-str'),
    path('special_int/<int:param>/', felipeapp_views.view_dinamica_int, name = 'dinamica-int'),
    path('redireciona/', felipeapp_views.redireciona, name='redireciona'),
    path('dtl/', felipeapp_views.special_dtl, name='retorna-html-dtl')
]

