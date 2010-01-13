from django.conf.urls.defaults import *
 
urlpatterns = patterns('picture.views',
    url(r'view/(?P<picture_id>\d+)/$', 'picture_view', name='picture_view'),
    )
 
