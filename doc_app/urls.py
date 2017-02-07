from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^print/$', views.document_print_view, name='document_print'),
    url(r'^create/$', views.document_create_view, name='document_create'),
    url(r'^$', views.document_list_view, name='document_list'),
    url(r'^(?P<id>\d+)/$', views.document_detail_view, name='document_detail'),
    url(r'^(?P<id>\d+)/print/$', views.document_print_view, name='document_print'),
]
