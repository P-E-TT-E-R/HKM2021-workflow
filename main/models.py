from django.db import models

class Schedule(models.Model):
    owner = models.CharField(max_length=32, null=False)
    """time = models.DateTimeField()
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    data = models.CharField(max_length=255)"""
    data_json = models.CharField(max_length=10000, default="{}")
    
class Room(models.Model):
    name = models.CharField(max_length=32, null=False)
    permission = models.CharField(max_length=32, null=True)
    description = models.CharField(max_length=255, null=True)
    availableFrom = models.TimeField(null=True)
    availableTo = models.TimeField(null=True)

class Project(models.Model):
    name = models.CharField(max_length=32, null=False)
    permission = models.CharField(max_length=32, null=True)
    description = models.CharField(max_length=255, null=True)
    waiting_json = models.CharField(max_length=10000, default="{}")
    in_progress_json = models.CharField(max_length=10000, default="{}")
    finished_json = models.CharField(max_length=10000, default="{}")

class Event(models.Model):
    name = models.CharField(max_length=32, null=False)
    permission = models.CharField(max_length=32, null=True)
    description = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(null=True)
    participating = models.CharField(max_length=10000, default="{}")
    data_json = models.CharField(max_length=10000, default="{}")