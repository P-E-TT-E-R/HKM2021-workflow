from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})

def panel(request):
    if request.user.is_authenticated:
        return render(request, 'main/controlpanel.html')
    else:
        raise PermissionDenied()
