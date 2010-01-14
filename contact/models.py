from django.db import models
from tagging.fields import TagField

class Contact(models.Model):
    """
    This record a contact request made from the website.
    """
    subject = models.CharField(max_length=55)
    email_address = models.EmailField()
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
