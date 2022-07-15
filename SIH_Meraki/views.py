from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def indexview(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse("admin:index"))
        
        elif request.user.groups.exists():
            group = request.user.groups.filter(user=request.user)[0]
            if group.name=="schools":
                return HttpResponseRedirect(reverse('schools:dashboard'))
            
            if group.name=="talukas":
                return HttpResponseRedirect(reverse('talukas:dashboard'))
    return render(request, 'index.html')