from django.shortcuts import get_object_or_404

from common.shortcuts import render_response

from models import Picture


def picture_view(request, picture_id):
    """
    Show the picture # picture_id if is_visible is True, overwise raise HTTP404 exception.
    """
    picture = get_object_or_404(Picture, pk=picture_id, is_visible=True)
    context = {'picture': picture,
               'current':'picture'}
    return render_response(request, 'picture/picture_view.html', context)
