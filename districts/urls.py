from django.urls import path, include, reverse_lazy
from . import views

app_name = 'districts'

urlpatterns = [
    # DISTRICT
    path(
        route= '',                    
        view = views.dashboardView,                
        name = 'dashboard'
    ),
    
    # SCHOOL
    path(
        route= 'register_school/',                    
        view = views.SchoolCreateView.as_view(),                
        name = 'register_school'
    ),
    path(
        route= 'manage_schools/',                    
        view = views.SchoolList.as_view(),                
        name = 'manage_schools'
    ),
    path(
        route= 'school_detail/<pk>/',                    
        view = views.SchoolDetail.as_view(),                
        name = 'school_detail'
    ),
]