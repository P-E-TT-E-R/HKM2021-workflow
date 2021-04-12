from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.db import connections
import json

# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})

def controlpanel(request):
    return render(request, 'main/controlpanel.html')