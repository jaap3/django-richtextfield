from django.contrib import admin

from testproject.testapp.forms import CommentForm
from testproject.testapp.models import Comment, Post


class CommentInline(admin.StackedInline):
    model = Comment
    form = CommentForm
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
