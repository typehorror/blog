from django.contrib import admin
from models import Contact

class ContactAdmin(admin.ModelAdmin):
    """
    Comment admin page
    """
    search_fields = ('email_address', 'body', 'subject')
    list_filter = ('creation_date',)
    list_display = ('email_address', 'subject', 'creation_date')

admin.site.register(Contact, ContactAdmin)
