from django.urls import path, include, reverse_lazy
from . import views

app_name = 'schools'

urlpatterns = [
    path('',                    views.dashboardView,                name='dashboard'),
    path('profile/',            views.profileView,                  name='profile'),
    path('update_profile_pic/', views.update_profile_pic,           name='update_profile_pic'),
    path('todays_meal/',        views.MealCreateView.as_view(),     name='todays_meal'),
    path('meal_detail/<pk>/',   views.MealDetailView.as_view(),     name='meal_detail'),
    path('student_details/',    views.studentDetailsView,           name='student_details'),
    path('create_students/',    views.StudentCreateView.as_view(),  name='create_students'),
    path('attendence/',         views.attendenceView,               name='attendence'),
    path('create_class/',       views.ClassCreateView.as_view(),    name='create_class'),
    path('class_detail/<pk>/',  views.ClassDetailView.as_view(),     name='class_detail'),
    path('manage_class/',       views.ClassListView.as_view(),      name='manage_class'),
    path('update_class/<pk>/',  views.ClassUpdateView.as_view(),   name='update_class'),
    path('delete_class/<pk>/',  views.ClassDeleteView,              name='delete_class'),
    
    

]
