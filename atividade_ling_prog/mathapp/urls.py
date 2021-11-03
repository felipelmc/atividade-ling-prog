from django.urls import path
from django.urls.conf import include
from mathapp import views as mathapp_views 

urlpatterns = [
    path('', mathapp_views.index, name='teste'),
    path('mathapp/', mathapp_views.matheus, name='mathapp'),
    path('mathapp2/', mathapp_views.matheus2, name='mathapp2'),
    path('mathapp3/', mathapp_views.matheus3, name='mathapp3')
]