from django.contrib import admin

from .models import *

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name_person', 'content', 'post', 'created_at', 'active')
    list_filter = ('created_at','active')
    search_fields = ('name_person', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=False)

admin.site.register(Post)