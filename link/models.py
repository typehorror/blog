from django.db import models
from tagging.fields import TagField

class Link(models.Model):
    """
    A link is used in order to generate a library of
interresting content thru the web
    """
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_visible = models.BooleanField()
    creation_date = models.DateField(auto_now_add=1)
    modification_date = models.DateField(auto_now=1, auto_now_add=1)
    logo = models.ImageField(max_length=100, upload_to="link_logo")
    link = models.URLField(max_length=200, verify_exists=1)
    tags = TagField(help_text='Enter tags separated by ,')


