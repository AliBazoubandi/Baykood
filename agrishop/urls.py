import agrishop.admin_config  # noqa
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from core.sitemaps import StaticViewSitemap, ProductSitemap, CategorySitemap, PostSitemap

sitemaps = {
    'static':     StaticViewSitemap,
    'products':   ProductSitemap,
    'categories': CategorySitemap,
    'posts':      PostSitemap,
}

urlpatterns = [
    path('admin/',      admin.site.urls),
    path('',            include('core.urls')),
    path('shop/',       include('shop.urls')),
    path('blog/',       include('blog.urls')),
    path('accounts/',   include('accounts.urls')),

    # SEO
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',  TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)