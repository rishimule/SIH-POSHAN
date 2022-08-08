from django.urls import path, include, reverse_lazy
from . import views

app_name = 'schools'

urlpatterns = [
    path('',                    views.dashboardView,                name='dashboard'),
    path('profile/',            views.profileView,                  name='profile'),
    path('todays_meal/',        views.MealCreateView.as_view(),     name='todays_meal'),
    path('meal_detail/<pk>/',   views.MealDetailView.as_view(),               name='meal_details'),
    path('attendence/',         views.attendenceView,               name='attendence'),
    path('student_details/',    views.studentDetailsView,           name='student_details'),
    path('register_students/',  views.registerStudentsView,         name='register_students'),
    path('create_students/',    views.StudentCreateView.as_view(),  name='create_students'),
    path('create_class/',       views.createClassView,              name='create_class'),
    path('update_class/<pk>/',   views.ClassUpdateView.as_view(),   name='update_class'),
    
    

]
