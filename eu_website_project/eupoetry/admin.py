from django.contrib import admin
from . import models


class RawVersesAdmin(admin.ModelAdmin):
    fileds = ["date_of_writing", "id"]
    # data_hierarchy = "date_of_writing"
    # ordering = ("date_of_writing",)
    pass


admin.site.register(models.RawVerses, RawVersesAdmin)

# Register your models here.
