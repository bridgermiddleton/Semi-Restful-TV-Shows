from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows/new$', views.addshowpage),
    url(r'^shows/create', views.createshow),
    url(r'shows/(?P<id>\d+)$', views.tvshowdetails),
    url(r'shows$', views.allshows),
    url(r'shows/(?P<id>\d+)/edit$', views.editshow),
    url(r'shows/(?P<id>\d+)/update$', views.updateshow),
    url(r'shows/(?P<id>\d+)/destroy$', views.destroyshow),
]

