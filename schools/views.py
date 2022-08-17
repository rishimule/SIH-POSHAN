from importlib.metadata import PackageNotFoundError
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_in_group_schools
from .forms import ClassForm, MealForm, StudentForm, SchoolForm,AddAttendenceForm
from django.utils import timezone
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Student, Class, School, Meal, Attendence
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def dashboardView(request):
    return render(request, 'schools/index.html')


@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def profileView(request):
    return render(request, 'schools/profile.html')


@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def attendenceView(request):
    return render(request, 'schools/attendence.html')



@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def update_profile_pic(request):
    myschool = request.user.schools
    print(request)
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=myschool)
        if form.is_valid():
            print(form)
            form.save()
            print('saved')
            return redirect('schools:profile')

    else:
        print('NO POST REQUEST')
        form = SchoolForm(instance=myschool)
        print(type(form))
        return render(request, 'schools/update_profile_pic.html', {'form': form})


class ClassCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = "schools/create_new_class.html"
    success_url: reverse_lazy('schools:dashboard')

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        return cond1

    def form_valid(self, form):
        form.instance.school = self.request.user.schools
        print('this validity')
        return super().form_valid(form)


class ClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Class
    form_class = ClassForm
    template_name = "schools/update_class.html"
    # success_url = reverse_lazy('schools:dashboard')

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        cond2 = self.request.user.schools.classes.filter(
            pk=self.kwargs['pk']).exists()
        return cond1 and cond2


@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def ClassDeleteView(request, pk):
    getclass = get_object_or_404(Class, pk=pk)
    if request.user.schools.classes.filter(pk=pk).exists():
        getclass.delete()
        return HttpResponseRedirect(reverse('schools:manage_class'))
    else:
        return render(request, '403.html')


class ClassDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Class
    template_name = "schools/class_detail.html"
    context_object_name = 'class'

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        cond2 = self.request.user.schools.classes.filter(
            pk=self.kwargs['pk']).exists()
        return cond1 and cond2

    def get_context_data(self, **kwargs):
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        myclass = get_object_or_404(Class, pk=self.kwargs['pk'])
        context["student_list"] = myclass.students.all()
        return context


class ClassListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    model = Class
    template_name = "schools/manage_class.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_list'] = self.request.user.schools.classes.all()
        return context

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        return cond1


class MealDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Meal
    context_object_name = 'meal'
    template_name = "schools/meal_detail.html"

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        cond2 = self.request.user.schools.meals.filter(
            pk=self.kwargs['pk']).exists()
        return cond1 and cond2


class MealCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Meal
    fields = '__all__'
    template_name = "schools/todays-meal.html"
    success_url: reverse_lazy('schools:dashboard')

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        return cond1

    def form_valid(self, form):
        form.instance.school = self.request.user.schools
        print('this validity')
        return super().form_valid(form)


class StudentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "schools/register_new_students.html"

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        return cond1

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['current_class'].queryset = self.request.user.schools.classes.all()
        return form

class StudentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Student
    template_name = "schools/student_detail.html"
    context_object_name = 'student'
 
    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        mystudent = get_object_or_404(Student, pk=self.kwargs['pk'])
        cond2 = mystudent.current_class.school.user == self.request.user
        return cond1 and cond2   
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "schools/update_student.html"
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['current_class'].queryset = self.request.user.schools.classes.all()
        return form

class AttendenceView(TemplateView):
    template_name = "schools/attendence.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form1 = AddAttendenceForm(self.request.user)
        context['form1'] = form1
        return context

def addAtt(request, date, myclass):
    return HttpResponseRedirect(render('home'))

def redirect_to_add_attendenceView(request):
    if request.method == 'POST':
        data = request.POST
        date = data['date']
        print(date)
        myclass = data['myclass']
        print(data)
        return redirect(reverse('schools:addAtt',  kwargs={'date':date, 'myclass':myclass}))   
