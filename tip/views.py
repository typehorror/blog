from django.shortcuts import get_object_or_404

from common.shortcuts import render_response
from common.utils import paginate

from models import Tip


def tip_view(request, tip_id):
    """
    show a list of picture
    """
    kwargs = {'pk': tip_id}
    # does not allow visitor to see not visible tip
    # this trick allow staff to preview tips they wrote
    if not request.user.is_staff:
        kwargs['is_visible'] = True
    tip = get_object_or_404(Tip,**kwargs)
    context = {'tip': tip,
               'current':'tips'}
    return render_response(request, 'tip/tip_view.html', context)

def tips_view(request):
    """
    show a list of picture
    """
    tips = Tip.objects.filter(is_visible=True).order_by("-creation_date")
    tips = paginate(tips, request, 3)
    context = {'tips': tips,
               'current':'tips'}
    return render_response(request, 'tip/tips_view.html', context)
