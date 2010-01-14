from django.shortcuts import get_object_or_404

from common.shortcuts import render_response

from models import Article, FeaturedArticle

def homepage(request):
    """
    Display some featured articles, most recent article 
    and some tips.
    """
    featured = FeaturedArticle.objects.filter(is_visible=True).order_by('?')
    if len(featured):
        featured = featured[0]
        
    articles = Article.objects.all().select_related().order_by('-creation_date')[:4]
    context = {'featured': featured,
               'articles': articles}
    return render_response(request, 'homepage.html', context)

def article_view(request, article_id):
    """
    Show the article # article_id if is_visible is True, overwise raise HTTP404 exception.
    """
    article = get_object_or_404(Article, pk=article_id, is_visible=True)
    comments = article.comments.select_related().filter(sensored=False)
    context = {'user_form': article,
               'current':'blog'}
    return render_response(request, 'articles/article_view.html', context)
