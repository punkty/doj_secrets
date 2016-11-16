from django.conf.urls import url
from . import views           

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^secret$', views.secret, name='secret'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like'),
    url(r'^hotsecrets$', views.hotsecrets, name='hotsecrets'),
  ]
