from django.contrib import admin
from models import Article, Comment

class CommentAdmin(admin.ModelAdmin):
    """
    Comment admin page
    """
    search_fields = ('email_address', 'body')
    list_filter = ('status', 'creation_date')
    list_display = ('email_address', 'website', 'creation_date', 'status')

class CommentInline(admin.TabularInline):
    """
    Display the comment linked to the article on
    the article admin page.
    """
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    """
    Article admin page
    """
    search_fields = ('title','tags')
    list_filter = ('is_visible','modification_date')
    list_display = ('title','creation_date','modification_date','author')

    inlines = [CommentInline,]

admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
