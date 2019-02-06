from django.contrib import admin

from .models import PostRecord


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(PostRecord, BlogAdmin)
