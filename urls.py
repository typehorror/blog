from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^article/', include('article.urls')),
    (r'^picture/', include('picture.urls')),
    (r'^tip/', include('tip.urls')),
    (r'^contact/', include('contact.urls')),
    (r'^link/', include('link.urls')),

    # add haystack search engine 
    (r'^search/', include('haystack.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'redirect_to', {'url': '/article/home/'}),
    #url(r'^$', 'direct_to_template', {'template': 'construct.html'}, name='under_construction'),
    url(r'^about_me/$', 'direct_to_template', {'template': 'about_me.html', 'extra_context':{'current': 'about'}}, name='about_me'),
    )
