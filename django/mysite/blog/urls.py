from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
)
