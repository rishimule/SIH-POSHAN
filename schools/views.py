from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_in_group_schools
from .forms import ClassForm, MealForm,StudentForm
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Student,Class,School, Meal, Attendence
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




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
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('schools:dashboard', pk=post.pk)  
    
    else:
        form = ClassForm()
    return render(request, 'schools/create_new_class.html', {'form': form})

class ClassUpdateView(UpdateView):
    model = Class
    form_class = ClassForm
    template_name = "schools/update_class.html"
    success_url = reverse_lazy('schools:dashboard')



class ClassDetailView(LoginRequiredMixin, UserPassesTestMixin,DetailView):
    model = Class
    template_name = "schools/class_detail.html"
    context_object_name = 'class'
    
    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        cond2 = self.request.user.schools.classes.filter(pk = self.kwargs['pk']).exists()
        return cond1 and cond2

    def get_context_data(self, **kwargs):
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        myclass = get_object_or_404(Class, pk=self.kwargs['pk'])
        context["student_list"] = myclass.students.all()
        return context
    


class MealDetailView(DetailView):
    model = Meal
    context_object_name = 'meal'
    template_name = "schools/meal_detail.html"


class MealCreateView(CreateView):
    model = Meal
    fields = '__all__'
    template_name = "schools/todays-meal.html"
    success_url: reverse_lazy('schools:dashboard')
    
    def form_valid(self, form):
        form.instance.school = self.request.user.schools
        print('this validity')
        return super().form_valid(form)




class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "schools/register_new_students.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['current_class'].queryset = self.request.user.schools.classes.all()
        return form