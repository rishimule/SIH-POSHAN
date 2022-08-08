from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_in_group_talukas


# Create your views here.
@user_passes_test(is_in_group_talukas) 
def dashboardView(request):
    return  render(request, 'talukas/index.html')

@user_passes_test(is_in_group_talukas) 
def profileView(request):
    return  render(request, 'talukas/profile.html')

# @user_passes_test(is_in_group_talukas) 
def registerSchoolsView(request):
    return  render(request, 'talukas/register-school.html')


