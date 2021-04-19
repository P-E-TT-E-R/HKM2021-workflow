from django.contrib import admin
from .models import Room, Event, Project
# Register your models here.

@admin.register(Room)
class RoomControl(admin.ModelAdmin):
  list_display = [field.name for field in
Room._meta.get_fields()]

@admin.register(Event)
class EventControl(admin.ModelAdmin):
  list_display = [field.name for field in
Event._meta.get_fields()]

@admin.register(Project)
class ProjectControl(admin.ModelAdmin):
  list_display = [field.name for field in
Project._meta.get_fields()]