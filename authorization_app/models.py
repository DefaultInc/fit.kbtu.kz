from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class ExtendedUser(models.Model):
    contact_phone = models.CharField(max_length=128, null=True, blank=True)
    additional_info = models.CharField(max_length=256, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #add any field you need


def create_extended_user(sender, **kwargs):
    if kwargs["created"]:
        ExtendedUser.objects.get_or_create(user=kwargs["instance"])

post_save.connect(create_extended_user, sender=User)