from django.db import models
from tagging.fields import TagField

from django.db.models.signals import post_save

class Contact(models.Model):
    """
    This record a contact request made from the website.
    """
    subject = models.CharField(max_length=55)
    email_address = models.EmailField()
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

def new_contact(sender, instance, **kwargs):
    from django.core.mail import send_mail
    from django.conf import settings
    from django.core.urlresolvers import reverse

    from django.contrib.sites.models import Site

    current_site = Site.objects.get_current()
    change_url = reverse('admin:contact_contact_change', args=(instance.id,))
    send_mail('New contact on the website',
              'Please check the website at http://%s%s' % (current_site.domain, change_url),
              'noreply@debrice.com',
              [ email for name, email in settings.MANAGERS])
 

post_save.connect(new_contact, sender=Contact)
