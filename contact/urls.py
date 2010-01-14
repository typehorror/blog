from django.conf.urls.defaults import *
 
urlpatterns = patterns('contact.views',
    url(r'form/$', 'contact_view', name='contact_view'),
    url(r'sent/$', 'contact_message_sent_view', name='contact_message_sent_view'),
    )
 
