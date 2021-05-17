from django.contrib import admin
from .models import Interest

class InterestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "content", "topic", "interest_date")
    list_display_links = ("id", "name")
    search_fields = ("name", "topic", "content")
    list_per_page = 25

admin.site.register(Interest, InterestAdmin)