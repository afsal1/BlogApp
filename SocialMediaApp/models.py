from django.db import models
from django.contrib.auth.models import User



class Feeds(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    content = models.TextField()
    
    