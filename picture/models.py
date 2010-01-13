from django.db import models
from tagging.fields import TagField

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to="picture")
    is_visible = models.BooleanField(default=False)
    tags = TagField(help_text='Enter tags separated by ,')
    creation_date = models.DateTimeField(auto_now_add=True)

    @models.permalink
    def get_absolute_url(self):
        return ('picture.views.picture_view', [self.pk])

    def __unicode__(self):
        return u'%s' % self.title
