from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
    content = models.TextField(max_length=4096, null=True, blank=True)
    #depends on implementation

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)