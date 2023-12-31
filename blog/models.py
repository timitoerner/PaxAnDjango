from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="postsImg")
    imgAlt = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datePosted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    