from django.conf.urls.defaults import *
 
urlpatterns = patterns('article.views',
    url(r'view/(?P<article_id>\d+)/$', 'article_view', name='article_view'),
    url(r'home/$', 'homepage', name='homepage'),
    )
 
