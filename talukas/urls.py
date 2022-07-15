from django.urls import path, include, reverse_lazy
from . import views

app_name = 'talukas'

urlpatterns = [
    path('', views.dashboardView, name='dashboard'),
    path('profile/', views.profileView, name='profile'),
    path('register_schools/', views.registerSchoolsView, name='register_schools'),
    

]
