from django.contrib import admin
from .models import *


class OfferMessageAdmin(admin.ModelAdmin):
    list_display = ('name_of_user', 'category', 'media_files', 'content', 'sent', 'reviewed', 'fixed')
    list_display_links = ('name_of_user', 'content', 'sent')
    search_fields = ('name_of_user', 'content', 'sent')


admin.site.register(OfferMessage, OfferMessageAdmin)
