from django.urls import path, include, reverse_lazy
from .views import StateCreateView

app_name = 'states'

urlpatterns = [
    path('create_new/', StateCreateView.as_view(), name='create'), 
    
    ]


    
