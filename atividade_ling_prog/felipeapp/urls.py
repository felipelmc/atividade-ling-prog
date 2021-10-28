from django.urls import path
from django.urls.conf import include
from felipeapp import views as felipeapp_views 

urlpatterns = [
    path('', felipeapp_views.index, name='teste'),
    path('felipeapp/', felipeapp_views.felipe, name='felipeapp')
]

