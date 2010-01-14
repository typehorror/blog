from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from common.shortcuts import render_response

from models import Article, FeaturedArticle

def paginate(records, request):
    page = request.GET.get('page', '1')
    paginator = Paginator(records, 6)
 
    try:
        page = int(page)
    except ValueError:
        page = 1
 
    try:
        records = paginator.page(page)
    except (EmptyPage, InvalidPage):
        records = paginator.page(paginator.num_pages)
    return records

def homepage(request):
    """
    Display some featured articles, most recent article 
    and some tips.
    """
    featured = FeaturedArticle.objects.filter(is_visible=True).order_by('?')
    if len(featured):
        featured = featured[0]
        
    articles = Article.objects.all().select_related().order_by('-creation_date')[:4]
    context = {'current': 'home',
               'featured': featured,
               'articles': articles}
    return render_response(request, 'homepage.html', context)

def article_archive_view(request):
    articles = Article.objects.filter(is_visible=True).order_by("-modification_date")

    articles = paginate(articles, request)
    context = {'articles': articles,
               'current':'archive'}
    return render_response(request, 'article/archive.html', context)


def article_view(request, article_id):
    """
    Show the article # article_id if is_visible is True, overwise raise HTTP404 exception.
    """
    article = get_object_or_404(Article, pk=article_id, is_visible=True)
    comments = article.comments.select_related().exclude(status='censored')
    context = {'article': article,
               'current':'blog'}
    return render_response(request, 'article/article_view.html', context)
