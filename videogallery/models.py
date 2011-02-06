from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class VideoFile(models.Model):
    videofile = models.FileField(upload_to='media/')

class Video(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    videofile = models.ForeignKey(VideoFile)
