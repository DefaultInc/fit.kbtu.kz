from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Claim(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    reason = models.CharField(max_length=256, null=True, blank=True)
    content = models.TextField(max_length=4096, null=True, blank=True)
    #depends on implementation

    def __unicode__(self):
        """
        returns title of the post.
        """
        return self.title

    def __str__(self):
        """
        returns title of the post.
        """
        return self.title

    def get_absolute_url(self):
        """
        returns absolute url of the post.
        """
        return reverse("doc_app:document_detail", kwargs={"id": self.id})

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE, null=True, blank=True)