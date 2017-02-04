from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from auth_app.models import ExtendedUser
from django.contrib.auth.models import User


# MVC pattern

def upload_location(instance, filename):
    """
    Making location for uploaded files (images)
    :return: making for everypost unique folder (based on post id),
    and uploading image to the folder with original filename.
    #Uploading image to the special location: (id of the post)/(image name)
    """
    return "%s/%s" % (instance.id, filename)

class Post(models.Model):
    """
    Main class for news field, main CRUD and other things, just read a comments and names of the variables.
    """
    # checking for the user (if not admin (superuser) then he can not create,update or delete)
    author = models.ForeignKey(User, default=1)
    # title field
    title = models.CharField(max_length=120, null=True, blank=True)
    # image field
    image = models.ImageField(upload_to=upload_location, null=True, blank=True,
                              width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    # content field
    content = models.TextField(null=True, blank=True)
    # updated field (when post will be update it changes time)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # timestamp
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

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
        return reverse("news_app:post_detail", kwargs={"id": self.id})

    class Meta:
        """
        latest news on the top
        """
        ordering = ["-timestamp", "-updated"]


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField(max_length=200)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-id"]
