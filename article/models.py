from django.db import models
from tagging.fields import TagField

from django.db.models.signals import post_save

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
    picture = models.ForeignKey('picture.Picture', related_name='articles')

    @models.permalink
    def get_absolute_url(self):
        return ('article.views.article_view', [self.pk])

    def __unicode__(self):
        return u'%s' % self.title

class FeaturedArticle(models.Model):
    """
    This record corresponds to the featured article actually display on the 
    home page.
    """
    article = models.ForeignKey(Article, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    is_visible = models.BooleanField(default=False)

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

def new_comment(sender, instance, **kwargs):
    from django.core.mail import send_mail
    from django.conf import settings
    from django.core.urlresolvers import reverse

    from django.contrib.sites.models import Site

    current_site = Site.objects.get_current()
    change_url = reverse('admin:article_comment_change', args=(instance.id,))
    send_mail('New comment on the website',
              'Please check the website at http://%s/%s' % (current_site.domain, change_url),
              'noreply@debrice.com',
              [ email for name, email in settings.MANAGERS])
 

post_save.connect(new_comment, sender=Comment)
