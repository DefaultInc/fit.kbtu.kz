from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Post belongs to one author
class Post(models.Model):
    header = models.CharField(max_length=128, null=True, blank=True)
    content = models.TextField(max_length=4096, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

#Commentary belongs to one author and one post
class Commentary(models.Model):
    content = models.TextField(max_length=4096, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)