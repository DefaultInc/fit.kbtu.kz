from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import ExtendedUser


# Register your models here.

class AbstractUserInline(admin.StackedInline):
    model = ExtendedUser
    can_delete = False
    verbose_name_plural = 'ExtendedUser'


class UserAdmin(BaseUserAdmin):
    inlines = (AbstractUserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
