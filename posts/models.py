from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# MVC pattern

#Uploading image to the special location: (id of the post)/(image name)
def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Post(models.Model):
    #title field
    title = models.CharField(max_length=120)
    #image field
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    #content field
    content = models.TextField()
    #updated field (when post will be update it changes time)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    #timestamp
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
    #latest posts on the top

    class Meta:
        ordering = ["-timestamp", "-updated"]