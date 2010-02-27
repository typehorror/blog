from haystack.indexes import *
from haystack import site

from models import Picture

class PictureIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    pub_date = DateTimeField(model_attr='creation_date')

    def get_queryset(self):
        return Picture.objects.filter(is_visible=True)

site.register(Picture, PictureIndex)
