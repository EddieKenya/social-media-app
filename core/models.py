from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=100,blank=True)
    second_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True) 
    profileimg = models.ImageField(upload_to='profileimg',default='blank-prof.jpg')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username

class Tweets (models.Model):
    content = models.TextField(blank=True, null=True)
    images_video = models.FileField(upload_to='postedfiles', blank=True, null=True)


# Create your models here.
