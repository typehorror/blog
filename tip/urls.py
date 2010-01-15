from django.conf.urls.defaults import *
 
urlpatterns = patterns('tip.views',
    url(r'list/$', 'tips_view', name='tips_view'),
    url(r'view/(?P<tip_id>\d+)/$', 'tip_view', name='tip_view'),
    )
 
