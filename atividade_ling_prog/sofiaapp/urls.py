from django.urls import path
from sofiaapp import views as views

urlpatterns = [
    path('', views.index, name='index'),
    #path('sofiaapp/', views.sofia, name='sofiaapp'),
    #path('laks/', views.laks, name='sofiaapp'),
    #path('vitz/', views.vitz, name='sofiaapp'),
    path('special_str/<str:param>/', views.view_dinamica_str, name = 'dinamica-str'),
    path('special_int/<int:param>/', views.view_dinamica_int, name = 'dinamica-int'),
    path('redireciona/', views.redireciona, name='redireciona'),
    path('dtl/', views.special_dtl, name='retorna-html-dtl'),
]