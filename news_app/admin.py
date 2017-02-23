from django.contrib import admin
from .models import Post, Comment, PostType


class PostModelAdmin(admin.ModelAdmin):
    """
    Admin fields
    """
    list_display = ["title", "updated", "timestamp", "post_type", ]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]

    search_fields = ["title", "content"]

    class Meta:
        model = Post


class CommentModelAdmin(admin.ModelAdmin):
    """
    Admin fields
    """
    list_display = ["id", "content", ]

    class Meta:
        model = Comment

admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(PostType)
