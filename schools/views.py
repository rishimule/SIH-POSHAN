from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_in_group_schools
from .forms import ClassForm, MealForm,StudentForm
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView
from .models import Student,Class,School, Meal, Attendence
from django.urls import reverse, reverse_lazy




# Create your views here.
@user_passes_test(is_in_group_schools) 
def dashboardView(request):
    return  render(request, 'schools/index.html')

@user_passes_test(is_in_group_schools) 
def registerStudentsView(request):
    return  render(request, 'schools/register-students.html')

@user_passes_test(is_in_group_schools) 
def profileView(request):
    return  render(request, 'schools/profile.html')

@user_passes_test(is_in_group_schools) 
def attendenceView(request):
    return  render(request, 'schools/attendence.html')

@user_passes_test(is_in_group_schools) 
def studentDetailsView(request):
    return  render(request, 'schools/blank.html')

def createClassView(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('schools:dashboard', pk=post.pk)  
    
    else:
        form = ClassForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@user_passes_test(is_in_group_schools) 
def todaysMealView(request):
    
    if request.method == "POST":
        form = MealForm(request.POST,  request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('schools:dashboard', pk=post.pk)  
    
    else:
        form = MealForm()
    return render(request, 'schools/todays-meal.html', {'form': form})


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "schools/register_new_students.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['current_class'].queryset = self.request.user.schools.classes.all()
        return form