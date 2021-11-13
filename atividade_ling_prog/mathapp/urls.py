from django.urls import path
from django.urls.conf import include
from mathapp import views as mathapp_views 

urlpatterns = [
    path('', mathapp_views.index, name='teste'),
    path('mathapp/', mathapp_views.matheus, name='mathapp'),
    path('mathapp2/', mathapp_views.matheus2, name='mathapp2'),
    path('mathapp3/', mathapp_views.matheus3, name='mathapp3'),
    path('redireciona/<argumento>', mathapp_views.redireciona, name='redireciona'),
    path('special/', mathapp_views.redireciona),
    path('special/<int:param>', mathapp_views.view_dinamica_int, name='dinamica_int'),
    path('special/<str:param>', mathapp_views.view_dinamica_str, name='dinamica_str'),
    path('dtl', mathapp_views.special_dtl, name='retorna-html-dtl')
]