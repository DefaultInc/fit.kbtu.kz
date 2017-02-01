from django.conf.urls import url
from django.contrib import admin


from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    comment_delete,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^edit/(?P<id>\d+)/$', post_update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', post_delete, name='delete'),
    url(r'^comment_delete/(?P<id>\d+)/(?P<ins>\d+)$', comment_delete, name='comment_delete'),
]
