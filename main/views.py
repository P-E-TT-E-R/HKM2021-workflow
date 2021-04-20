from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from .models import Room, Event, Project
# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})

def panel(request):
    if request.user.is_authenticated:
        return render(request, 'main/panel.html')
    else:
        raise PermissionDenied()
def schedule(request):
    if request.user.is_authenticated:
        return render(request, 'main/schedule.html')
    else:
        raise PermissionDenied()
def projects(request):
    if request.user.is_authenticated:
        return render(request, 'main/projects.html')
    else:
        raise PermissionDenied()
def rooms(request):
    if request.user.is_authenticated:
        return render(request, 'main/rooms.html')
    else:
        raise PermissionDenied()
def events(request):
    if request.user.is_authenticated:
        rows = Event.objects.all().order_by("-date")
        return render(request, 'main/events.html', {"rows":rows})
    else:
        raise PermissionDenied()
