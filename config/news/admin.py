from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Post

# Register your models here.

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'views', 'created', 'updated', 'category', 'published', 'get_image')
    list_display_links = ('name', 'pk')
    list_editable = ('published', 'category')
    list_filter = ('category', 'published')
    search_fields = ('pk', 'name', 'content')
    list_per_page = 10
    readonly_fields = ('views',)

    def get_image(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" width="150px">')
        else:
            return '-'

    get_image.short_description = "Rasmi"


admin.site.register(Post, PostAdmin)