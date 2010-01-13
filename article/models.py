from django.db import models
from tagging.fields import TagField

from django.contrib.auth.models import User

REPORT_CHOICES = (
    ('na', 'N/A'),
    ('reported', 'Reported'),
    ('validated', 'Validated'),
    ('censored', 'Censored'),
    )

class Article(models.Model):
    """
    This model manage blog's articles. Every article has a body (full 
    content of the article), a preview (a presentation of the article), 
    an author and some tags. The is_visible property indicates if the 
    article is available to the public.
    """
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    preview = models.TextField()
    body = models.TextField()
    tags = TagField(help_text='Enter tags separated by ,')
    is_visible = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    @models.permalink
    def get_absolute_url(self):
        return ('article.views.article_view', [self.pk])


class Comment(models.Model):
    """
    represent a comment on an article. A comment can also be
    a reply to another comment.
    """
    article = models.ForeignKey(Article, related_name='comments')
    reply_to = models.ForeignKey('self', null=True, blank=True, related_name='replies')
    name = models.CharField(max_length=55)
    email_address = models.EmailField()
    website = models.URLField(verify_exists=True, blank=True)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=REPORT_CHOICES, default='na')

