from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list'),
    url(r'^create/$', views.post_create_view, name='post_create'),
    url(r'^(?P<id>\d+)/$', views.post_detail_view, name='post_detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update_view, name='post_update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete_view, name='post_delete'),
    url(r'^comment_delete/(?P<comment_id>\d+)/(?P<post_id>\d+)$', views.comment_delete_view, name='comment_delete'),
]