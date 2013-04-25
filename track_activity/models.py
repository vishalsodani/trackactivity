from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length = 100)
    has_end_time = models.BooleanField(default = 0, choices = ((1,'YES'),(0,'NO')))
    user = models.ForeignKey(User,editable=False)

class TimeTrack(models.Model):
    activity = models.ForeignKey(Activity)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True)
