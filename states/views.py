from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import StateForm
from .models import State
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class StateCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = State
    form_class = StateForm
    template_name = "states/register_state.html"
    success_url = reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.is_superuser