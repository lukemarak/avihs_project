from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^ipc510/$', views.ipc510, name='ipc510'),
    url(r'^ipc610/$', views.ipc610, name='ipc610'),
    url(r'^acp4000/$', views.acp4000, name='acp4000'),
    url(r'^acp4360/$', views.acp4360, name='acp4360'),
    url(r'^acp2000/$', views.acp2000, name='acp2000'),
]
