from django.conf.urls.defaults import *
 
urlpatterns = patterns('tip.views',
    url(r'list/$', 'tips_view', name='tips_view'),
    )
 
