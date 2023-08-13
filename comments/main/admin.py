from django.contrib import admin
from .models import CommentForm

@admin.register(CommentForm)
class CommentFormAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'home_page', 'parent_comment', 'created_at')
