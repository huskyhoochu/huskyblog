from django.db import models
from django.contrib import admin

from markdownx.widgets import AdminMarkdownxWidget

from blog.models import Post, Category, Image


# markdownx 구현을 위한 admin 세팅
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget}
    }
    list_display = ['id', 'title', 'category', 'published_date', 'created_date']
    list_display_links = ['title']
    list_editable = ['category']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'title']
    list_display_links = ['title']

# admin.site.register(Image)
