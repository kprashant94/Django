from django.conf.urls import include, url
from . import views

app_name = 'dsnalgo'

urlpatterns = [
	#/dsnalgo/
    url(r'^$', views.dsnalgo, name='index'),

    #/dsnalgo/1/
    url(r'^(?P<article_id>[0-9]+)/$', views.article_detail, name='article-detail'),

    #/dsnalgo/1/2/
    url(r'^(?P<article_id>[0-9]+)/(?P<sub_article_id>[0-9]+)/$', views.sub_article_detail, name='sub_article-detail'),
]
