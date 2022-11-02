from django.contrib import admin
from . import models


class RawVersesAdmin(admin.ModelAdmin):
    # data_hierarchy = "date_of_writing"
    # ordering = ("date_of_writing",)
    pass


admin.site.register(models.RawVerses)
admin.site.register(models.IdWord)
admin.site.register(models.IdJsonWords)

# Register your models here.
