from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page
from views import tips_view

urlpatterns = patterns('tip.views',
    url(r'list/$', cache_page(tips_view, 3600), name='tips_view'),
    url(r'view/(?P<tip_id>\d+)/$', 'tip_view', name='tip_view'),
    )
 
