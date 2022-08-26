from re import template
from django.urls import path, include, reverse_lazy
from . import views

app_name = 'schools'

urlpatterns = [
    # SCHOOL
    path('',                    views.dashboardView,                name='dashboard'),
    path('profile/',            views.profileView,                  name='profile'),
    path('update_profile_pic/', views.update_profile_pic,           name='update_profile_pic'),
    path('location_not_found/', views.TemplateView.as_view(template_name = 'schools/location_not_found.html'),           name='location_not_found'),
    
    # MEAL
    path('todays_meal/',        views.mealCreateView,               name='todays_meal'),
    path('meal_list/',          views.MealListView.as_view(),               name='meal_list'),
    path('meal_detail/<pk>/',   views.MealDetailView.as_view(),     name='meal_detail'),
    
    # STUDENT
    path('create_students/',    views.StudentCreateView.as_view(),  name='create_students'),
    path('student_detail/<pk>/',views.StudentDetailView.as_view(),  name='student_detail'),
    path('update_student/<pk>/', views.StudentUpdateView.as_view(),  name='update_student'),
    path('add_health_record/<studentpk>/', views.add_healthrecord,  name='add_health_record'),
    path('healthrecord_detail/<pk>/',views.HealthRecordDetailView.as_view(),  name='healthrecord_detail'),
    path('cognitive/',views.TemplateView.as_view(template_name = 'schools/cognitive.html'),  name='cognitive'),

    
    # CLASS
    path('create_class/',       views.ClassCreateView.as_view(),    name='create_class'),
    path('class_detail/<pk>/',  views.ClassDetailView.as_view(),    name='class_detail'),
    path('manage_class/',       views.ClassListView.as_view(),      name='manage_class'),
    path('update_class/<pk>/',  views.ClassUpdateView.as_view(),    name='update_class'),
    path('delete_class/<pk>/',  views.ClassDeleteView,              name='delete_class'),
    
    # ATTENDENCE
    path(
        'attendence/',        
        views.AttendenceView.as_view(),     
        name='attendence'
        ),
    path(
        'addAtt/<myclass>/<date>/',        
        views.addAtt,     
        name='addAtt'
        ),
    path(
        'redirect_to_add_attendence/',        
        views.redirect_to_add_attendenceView, 
        name='redirect_to_add_attendence'
        ),

]
