from haystack.indexes import *
from haystack import site

from models import Article

class ArticleIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr='author')
    pub_date = DateTimeField(model_attr='creation_date')

    def get_queryset(self):
        return Article.objects.filter(is_visible=True)

site.register(Article, ArticleIndex)
