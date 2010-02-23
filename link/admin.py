from django.contrib import admin
from models import *


class LinkAdmin(admin.ModelAdmin):
    """
    Link admin class
    """
    search_fields = ('title', 'description', 'tags')
    list_filter = ('creation_date','modification_date', 'is_visible') 
    list_display = ('title', 'link', 'is_visible', 'creation_date','modification_date')

admin.site.register(Link, LinkAdmin)

