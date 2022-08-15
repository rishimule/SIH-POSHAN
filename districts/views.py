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

# Create your views here.
# Create your views here.
# @user_passes_test(is_in_group_districts, login_url='/')
# @login_required
def dashboardView(request):
    return render(request, 'districts/dashboard.html')