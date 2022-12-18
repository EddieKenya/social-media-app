from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


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

class Post (models.Model):
    user = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    posts_image= models.ImageField(upload_to='post_images', blank=True, null=True)
    caption = models.TextField(blank=True,null=True)
    no_of_likes = models.IntegerField(default=0)
    post_no_comments =models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user

class likes(models.Model):
    username = models.CharField(max_length=50)
    post_liked = models.CharField(max_length=500)

    def __str__(self):
        return self.post_liked

class Comments(models.Model):
    username = models.CharField(max_length=50)
    post_commented= models.CharField(max_length=500, default='post_id')
    comments= models.TextField(blank=True
    )

    def __str__(self):
        return self.username



# Create your models here.
