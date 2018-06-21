from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^board$', views.board, name='board'),
    url(r'^add_client$', views.add_client, name='add_client'),
    url(r'^add_chasis$', views.add_chasis, name='add_chasis'),
    url(r'^create_config$', views.create_config, name='create_config'),
    url(r'^detail$', views.detail, name='detail'),
]
