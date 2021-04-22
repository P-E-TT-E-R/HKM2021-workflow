from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from .models import Room, Event, Project
import json
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
        projects = Project.objects.all()
        myprojects = []
        for project in projects:
            if request.user.has_perm(project.permission):
                myprojects.append(project)

        waiting = json.loads(myprojects[0].waiting_json)
        inprogress = json.loads(myprojects[0].in_progress_json)
        finished = json.loads(myprojects[0].finished_json)
        return render(request, 'main/projects.html', {"waiting":waiting,"in_progress":inprogress,"finished":finished})
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
