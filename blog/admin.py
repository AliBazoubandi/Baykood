from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display        = ['name', 'post_count']
    prepopulated_fields = {'slug': ('name',)}

    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'تعداد مقالات'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ['cover_preview', 'title', 'tag_list', 'is_published', 'published_at']
    list_display_links  = ['cover_preview', 'title']
    list_filter         = ['is_published', 'tags']
    list_editable       = ['is_published']
    search_fields       = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal   = ['tags']
    ordering            = ['-published_at']

    fieldsets = (
        ('محتوا', {
            'fields': ('title', 'slug', 'body', 'cover_image')
        }),
        ('ویدیو', {
            'fields': ('video_url',),
            'description': 'لینک YouTube یا Instagram را اینجا وارد کنید'
        }),
        ('تنظیمات', {
            'fields': ('tags', 'is_published')
        }),
    )

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="height:48px; width:72px; object-fit:cover; border-radius:6px;" />',
                obj.cover_image.url
            )
        return '—'
    cover_preview.short_description = ''

    def tag_list(self, obj):
        return ', '.join(t.name for t in obj.tags.all())
    tag_list.short_description = 'تگ‌ها'