from django.contrib import admin
from .models import Post, Comment, Like


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # empty forms nahi dikhenge
    readonly_fields = ['author', 'created_at']


class LikeInline(admin.TabularInline):
    model = Like
    extra = 0
    readonly_fields = ['user']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'total_comments', 'total_likes']
    list_filter = ['author', 'created_at']
    search_fields = ['title', 'content', 'author__username']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    inlines = [CommentInline, LikeInline]  # Post ke andar hi comments/likes dikhenge

    def total_comments(self, obj):
        return obj.comment_set.count()
    total_comments.short_description = 'Comments'

    def total_likes(self, obj):
        return obj.like_set.count()
    total_likes.short_description = 'Likes'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at', 'short_content']
    list_filter = ['author', 'created_at']
    search_fields = ['content', 'author__username', 'post__title']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    short_content.short_description = 'Content'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user']
    list_filter = ['user']
    search_fields = ['post__title', 'user__username']
# Register your models here.
