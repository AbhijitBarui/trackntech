from django.contrib import admin
from .models import Vote

class VoteAdmin(admin.ModelAdmin):
    list_display=("id",)

admin.site.register(Vote, VoteAdmin)