from django.db import models

# Create your models here.
class UID (models.Model):
    name = models.TextField(unique = True)
    email = models.EmailField(unique = True)
    password = models.TextField()

