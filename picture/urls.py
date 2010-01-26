from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page
from views import pictures_view
 
urlpatterns = patterns('picture.views',
    url(r'view/(?P<picture_id>\d+)/$', 'picture_view', name='picture_view'),
    url(r'list/$', cache_page(pictures_view, 3600), name='pictures_view'),
    )
 
