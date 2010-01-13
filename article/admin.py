from django.contrib import admin
from models import Article, Comment, FeaturedArticle

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

class FeaturedArticleAdmin(admin.ModelAdmin):
    """
    Featured Article admin page
    """
    list_filter = ('is_visible','modification_date')
    list_display = ('id', 'creation_date', 'is_visible')

admin.site.register(FeaturedArticle, FeaturedArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
