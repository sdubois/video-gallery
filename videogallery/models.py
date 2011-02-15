from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class VideoFile(models.Model):
    videofile = models.FileField(upload_to='media/')
    def __unicode__(self):
        return self.videofile

class Video(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    videofile = models.ForeignKey(VideoFile)
    def __unicode(self):
        return u'%s, %s' % (self.user.username, self.link.url)

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    videos = models.ManyToManyField(Video)
    def __unicode__(self):
        return self.name


