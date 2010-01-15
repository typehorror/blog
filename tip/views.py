from django.shortcuts import get_object_or_404

from common.shortcuts import render_response
from common.utils import paginate

from models import Tip


def tip_view(request, tip_id):
    """
    show a list of picture
    """
    tip = get_object_or_404(Tip,pk=tip_id,is_visible=True)
    context = {'tip': tip,
               'current':'tips'}
    return render_response(request, 'tip/tip_view.html', context)

def tips_view(request):
    """
    show a list of picture
    """
    tips = Tip.objects.filter(is_visible=True).order_by("-creation_date")
    tips = paginate(tips, request)
    context = {'tips': tips,
               'current':'tips'}
    return render_response(request, 'tip/tips_view.html', context)
