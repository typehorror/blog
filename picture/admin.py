from django.contrib import admin
from models import Picture

class PictureAdmin(admin.ModelAdmin):
    """
    Picture admin page
    """
    search_field = ('title', 'tags')
    list_filter = ('is_visible', 'creation_date')
    list_display = ('title', 'creation_date', 'is_visible', 'tags')

admin.site.register(Picture, PictureAdmin)
