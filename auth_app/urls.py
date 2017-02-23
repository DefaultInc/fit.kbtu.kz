from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^register/$', views.register, name='register'),
	url(r'^login/$', auth_views.login, {'template_name': 'auth_app/login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
]
