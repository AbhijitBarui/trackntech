from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "topic", "is_published", "content_date", "author")
    list_display_links = ("id", "title")
    list_filter = ("author",)
    list_editable = ("is_published",)
    search_fields = ("title", "description", "text_main", "topic")
    list_per_page = 25

admin.site.register(Content, ContentAdmin)