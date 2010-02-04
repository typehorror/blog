from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from common.shortcuts import render_response
from common.utils import paginate

from models import Contact
from forms import ContactForm

def contact_view(request):
    """
    Record a contact request from the website.
    """
    context = {'current': 'contact'}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return HttpResponseRedirect(reverse('contact_message_sent_view'))
        else:
            context['form']=form
    else:
        context['form']=ContactForm()
    context['unread'] = Contact.objects.filter(is_read=False).count()
    return render_response(request, 'contact/contact_view.html', context)

def contact_message_sent_view(request):
    return render_response(request, 'contact/contact_sent.html')
