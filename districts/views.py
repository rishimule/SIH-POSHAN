from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_in_group_districts
from django.utils import timezone
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from schools.models import School
from .forms import SchoolForm
from .models import District

# Create your views here.
# Create your views here.
@user_passes_test(is_in_group_districts, login_url='/')
@login_required
def dashboardView(request):
    return render(request, 'districts/dashboard.html')

class SchoolCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = School
    template_name = "districts/register_school.html"
    form_class = SchoolForm
    
    def form_valid(self, form):
        form.instance.district = self.request.user.districts
        return super().form_valid(form)
    
    def test_func(self):
        cond1 = is_in_group_districts(self.request.user)
        return cond1
    
class SchoolDetail(DetailView):
    model = School
    context_object_name= 'school'
    template_name='districts/school_detail.html'



class SchoolList(ListView):
    model = School
    template_name='districts/manage_schools.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_list'] = self.request.user.districts.schools.all()
        return context

class DistrictDetail(DetailView):
    model = District
    template_name='districts/manage_schools.html'
    context_object_name= 'district'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_list'] = self.request.user.schools.all()
        return context