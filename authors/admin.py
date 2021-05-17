from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display=("id", "name", "email", "phone", "hire_date", "is_mvp")
    list_editable = ("is_mvp",)
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25
admin.site.register(Author, AuthorAdmin)