from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404

from models import Link

def list_link(request):
    """
    Display a list of Link paginated
    """
    link_list = Link.objects.filter(is_visible=True)
    paginator = Paginator(link_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        link_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        link_list = paginator.page(paginator.num_pages)

    context = {'link_list': link_list,
               'current': 'link'}
    return render_to_response('link_list.html',
                              context,
                              context_instance=RequestContext(request))



