from django.contrib import admin
from .models import Thumbnails

admin.site.site_header = "Hex Ocean coding task"


class ThumbnailsAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)
# Register your models here.


admin.site.register(Thumbnails, ThumbnailsAdmin)
