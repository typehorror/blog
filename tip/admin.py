from django.contrib import admin
from models import Tip

class TipAdmin(admin.ModelAdmin):
    """
    Tip admin page
    """
    search_fields = ('title', 'body')
    list_filter = ('creation_date', 'is_visible')
    list_display = ('title', 'creation_date', 'is_visible')

admin.site.register(Tip, TipAdmin)
