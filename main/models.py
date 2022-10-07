from email.policy import default
from django.db import models

# Create your models here.


class Post(models.Model):
    body = models.TextField(max_length=300)

class Company(models.Model):
    twitter_id = models.Model

class Influencer(models.Model):
    twitter_id = models.CharField(max_length=250, blank=True, null=True )
    instagram_id = models.CharField(max_length=250, blank=True, null=True )
    rating = models.IntegerField(blank=True, default=0)
    twitter_username = models.CharField(max_length=250, blank=True, null=True )
    instagram_username = models.CharField(max_length=250, blank=True, null=True )


    def __str__(self):
        return str(self.id)
