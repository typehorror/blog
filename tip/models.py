from django.db import models
from django.contrib.auth.models import User

from tagging.fields import TagField

# Create your models here.
class Tip(models.Model):
    """
    This model manage blog's articles. Every article has a body (full 
    content of the article), a preview (a presentation of the article), 
    an author and some tags. The is_visible property indicates if the 
    article is available to the public.
    """
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    body = models.TextField()
    tags = TagField(help_text='Enter tags separated by ,')
    is_visible = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    @models.permalink
    def get_absolute_url(self):
        return ('tip.views.tip_view', [self.pk])

    def __unicode__(self):
        return u'%s' % self.title
