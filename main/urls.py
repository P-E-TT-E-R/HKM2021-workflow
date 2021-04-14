from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('panel', views.panel, name='panel'),
    path('schedule', views.schedule, name='schedule'),
    path('projects', views.projects, name='projects'),
    path('rooms', views.rooms, name='rooms'),
    path('events', views.events, name='events')
]