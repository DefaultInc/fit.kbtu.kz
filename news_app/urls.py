from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list_view, name='list'),
    url(r'^create/$', views.post_create_view, name='create'),
    url(r'^(?P<id>\d+)/$', views.post_detail_view, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update_view, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete_view, name='delete'),
]