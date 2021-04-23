from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from .models import Room, Event, Project, Schedule
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
        print("Pisaa")
        if  Schedule.objects.filter(owner=request.user.username):
            object = Schedule()
            object.owner = request.user.username
            object.data_json = ""
            return render(request, 'main/schedule.html')

        else:
            sched = Schedule.objects.filter(owner=request.user.username)
            data = json.loads(sched.data_json)
            week = 2
            print("Pisaa")
            data = json.loads(
                """{
                                "2":{
                                    "2":{
                                        "mon": {
                                          "0": "Zubár"
                                        }
                                      }
                                    }
                                }
                                    """
            )
            for day in data[str(week)]:
                day = data[str(week)][day]
                events = []
                for time in range(0,12):
                    if time in day:
                        events.append({"class":"colored","height":"3em","name":day[time]})
                    else:
                        events.append({"class": "", "height": "3em", "name":""})
                print(events)
            return render(request, 'main/schedule.html',{"sun": events, "mon": data["mon"], "tue": data["tue"], "wed": data["wed"], "thu": data["thu"], "fri": data["fri"], "sat": data["sat"]})
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
        arr = []
        for task in waiting:
            arr.append({'name': task, 'date': waiting[task]['date'], 'priority': waiting[task]['priority']})
        waiting = arr

        inprogress = json.loads(myprojects[0].in_progress_json)
        arr = []
        for task in inprogress:
            arr.append({'name': task, 'user': inprogress[task]['user'], 'priority': inprogress[task]['priority']})
        inprogress = arr

        finished = json.loads(myprojects[0].finished_json)
        arr = []
        for task in finished:
            arr.append({'name': task, 'user': finished[task]['user'], 'priority': finished[task]['priority']})
        finished = arr

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
