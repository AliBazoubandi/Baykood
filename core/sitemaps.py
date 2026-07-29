from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from shop.models import Product, Category
from blog.models import Post


class StaticViewSitemap(Sitemap):
    priority   = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['core:home', 'core:about', 'core:contact', 'shop:product_list', 'blog:post_list']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    priority   = 0.8
    changefreq = 'weekly'

    def items(self):
        return Product.objects.filter(is_available=True)

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    priority   = 0.6
    changefreq = 'monthly'

    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    priority   = 0.7
    changefreq = 'monthly'

    def items(self):
        return Post.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at