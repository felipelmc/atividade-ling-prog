from django.urls import path
from django.urls.conf import include
from mathapp import views as mathapp_views 

urlpatterns = [
    path('', mathapp_views.index, name='teste'),
    path('mathapp/', mathapp_views.matheus, name='mathapp')
]