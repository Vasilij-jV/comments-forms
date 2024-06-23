from django.contrib import admin
from .models import Post, Comment, ContactModelToAdmin, Article, CommentForArticle


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'message_to_admin')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(ContactModelToAdmin)
class ContactModelToAdmin(admin.ModelAdmin):
    list_display = ('sent_message',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
    list_filter = ('created', 'author')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    ordering = ('created', 'title',)


@admin.register(CommentForArticle)
class CommentForArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('name', 'email', 'content')
