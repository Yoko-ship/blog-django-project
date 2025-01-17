from django.contrib import admin
from .models import Note


class AdminCustom(admin.ModelAdmin):
    fieldsets = [
        ("Text information",{"fields": ["title","content"]}),
        ("Date information",{"fields" : ["pub_date"]})
    ]
    list_display = ["title","content","pub_date"]
    list_filter = ["pub_date"]
    search_fields = ["content"]

admin.site.register(Note,AdminCustom)
# Register your models here.
