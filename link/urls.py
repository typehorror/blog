from django.conf.urls.defaults import *  

urlpatterns = patterns('link.views',
    url(r'list/link/$', 'list_link', name='link_link_list'),
    )
