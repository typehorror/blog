from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page
from views import homepage, article_archive_view
 
urlpatterns = patterns('article.views',
    url(r'view/(?P<article_id>\d+)/$', 'article_view', name='article_view'),
    url(r'home/$', cache_page(homepage, 3600), name='homepage'),
    url(r'archive/$',cache_page(article_archive_view, 3600), name='article_archive_view'),
    )
 
