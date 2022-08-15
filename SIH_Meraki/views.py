from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

class PlaceholderView(TemplateView):
    template_name = "placeholder.html"





def indexview(request):
    if request.user.is_authenticated:
        print('USER is AUTHENTICATED')
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse("admin:index"))
        
        elif request.user.groups.exists():
            group = request.user.groups.filter(user=request.user)[0]
            print(group)
            if group.name=="schools":
                return HttpResponseRedirect(reverse('schools:dashboard'))
            
            if group.name=="talukas":
                return HttpResponseRedirect(reverse('talukas:dashboard'))
            
            if group.name=="states":
                return HttpResponseRedirect(reverse('placeholder'))
            
            if group.name=="districts":
                print('DISTRICT FOUND')
                return HttpResponseRedirect(reverse('districts:dashboard'))
    return render(request, 'index.html')