from django.contrib import admin
from .models import *


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'title', 'media_files', 'published', 'rubric')
    list_display_links = ('user_name', 'title')
    search_fields = ('user_name', 'title', 'content')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user_name_comm', 'content_comm', 'published_comm', 'subject')
    list_display_links = ('user_name_comm', )
    search_fields = ('user_name_comm', 'content_comm')


admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Rubric)
