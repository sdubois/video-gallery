from django.db import models

# Create your models here.
class Video(models.Model):
    
    #FileField needs an upload_to parameter, i'll do it later
    #videoFile = models.FileField()
    
    videoTitle = models.TextField()
    videoTimestamp = models.DateTimeField()
    videoURL = models.URLField(unique = True)
    