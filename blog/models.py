from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام تگ')
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    class Meta:
        verbose_name        = 'تگ'
        verbose_name_plural = 'تگ‌ها'
        ordering            = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_list_by_tag', args=[self.slug])


class Post(models.Model):
    title        = models.CharField(max_length=300, verbose_name='عنوان')
    slug         = models.SlugField(max_length=300, unique=True, allow_unicode=True)
    body         = models.TextField(verbose_name='متن مقاله')
    cover_image  = models.ImageField(upload_to='blog/', blank=True, verbose_name='تصویر کاور')
    video_url    = models.URLField(blank=True, verbose_name='لینک ویدیو (YouTube / Instagram)')
    tags         = models.ManyToManyField(Tag, blank=True, verbose_name='تگ‌ها', related_name='posts')
    is_published = models.BooleanField(default=True, verbose_name='منتشر شده')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering            = ['-published_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_embed_url(self):
        """Converts a YouTube or Instagram URL into an embeddable URL."""
        url = self.video_url
        if not url:
            return None

        # YouTube: handle both youtu.be and youtube.com/watch?v= formats
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[-1].split('?')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        if 'youtube.com/watch' in url:
            from urllib.parse import urlparse, parse_qs
            parsed = urlparse(url)
            video_id = parse_qs(parsed.query).get('v', [None])[0]
            if video_id:
                return f'https://www.youtube.com/embed/{video_id}'
        if 'youtube.com/shorts/' in url:
            video_id = url.split('youtube.com/shorts/')[-1].split('?')[0]
            return f'https://www.youtube.com/embed/{video_id}'

        # Instagram: reels and posts
        if 'instagram.com/reel/' in url or 'instagram.com/p/' in url:
            clean = url.split('?')[0].rstrip('/')
            return f'{clean}/embed'

        return None