from haystack.indexes import *
from haystack import site

from models import Link

class LinkIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    pub_date = DateTimeField(model_attr='creation_date')

    def get_queryset(self):
        return Link.objects.filter(is_visible=True)

site.register(Link, LinkIndex)
