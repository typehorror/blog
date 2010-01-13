from django.shortcuts import get_object_or_404

from common.shortcuts import render_response

from models import Article


def article_view(request, article_id):
    """
    Show the article # article_id if is_visible is True, overwise raise HTTP404 exception.
    """
    article = get_object_or_404(Article, pk=article_id, is_visible=True)
    comments = article.comments.select_related().filter(sensored=False)
    context = {'user_form': article,
               'current':'blog'}
    return render_response(request, 'articles/article_view.html', context)
