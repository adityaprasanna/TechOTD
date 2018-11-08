from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

app_name='blog'
urlpatterns = [
 url(r'^$', views.home, name='home'),
 url(r'^techbuzz/$', views.post_list, name='post_list'),
 url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
 url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    views.post_detail,
    name = 'post_detail'),
 url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
 url(r'^home/$', views.home, name='home'),
 url(r'^featured/$', views.featured, name='featured'),
 url(r'^AboutUs/$', views.About, name='about'),

]
