from django.contrib import admin

from blog.models import Post, Category, Image


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'published_date', 'created_date']
    list_display_links = ['title']
    list_editable = ['category']

# admin.site.register(Post)
admin.site.register(Category)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
  list_display = ['id', 'post', 'title']
  list_display_links = ['title']

# admin.site.register(Image)
