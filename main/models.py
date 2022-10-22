from django.db import models

# Create your models here.

class Post(models.Model):
    body = models.CharField(max_length=200)
    primaryColor= models.CharField(max_length=7, default="#ffffff")
    secondaryColor= models.CharField(max_length=7, default="#ffffff")
