from django.db import models
from tagging.fields import TagField

# Create your models here.
class Picture(models.Model):
    title = models.Charfield(max_lenght=255)
    file = models.ImageField(upload_to="picture")
    is_visible = models.BooleanField(default=False)
    tags = TagField(help_text='Enter tags separated by ,')

    @models.permalink
    def get_absolute_url(self):
        return ('picture.views.picture_view', [self.pk])

