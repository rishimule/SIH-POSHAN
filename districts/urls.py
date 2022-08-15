from django.urls import path, include, reverse_lazy
from . import views

app_name = 'districts'

urlpatterns = [
    # DISTRICT
    path('',                    views.dashboardView,                name='dashboard'),
]