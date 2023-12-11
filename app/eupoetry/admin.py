from django.contrib import admin
from .models import RawVerses, EuPro


class RawVersesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Форма", {"fields": ["html_name", "title", "date_of_writing"]}),
        ("Содержание", {"fields": ["verses"]}),
    ]
    list_display = ["title", "html_name", "date_of_writing"]
    search_fields = ["verses"]

class EuProAdmin(admin.ModelAdmin):
    list_display = ["title", "html_name", "date_of_writing", "fact"]
    search_fields = ["title"]

admin.site.register(RawVerses, RawVersesAdmin)
admin.site.register(EuPro, EuProAdmin)

