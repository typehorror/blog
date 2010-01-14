from django.shortcuts import get_object_or_404

from common.shortcuts import render_response
from common.utils import paginate

from models import Tip


def tips_view(request):
    """
    show a list of picture
    """
    tips = Tip.objects.filter(is_visible=True).order_by("-creation_date")
    tips = paginate(tips, request)
    context = {'tips': tips,
               'current':'tips'}
    return render_response(request, 'tip/tips_view.html', context)
