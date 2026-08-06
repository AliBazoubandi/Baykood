from django.contrib import admin

admin.site.site_header  = 'پنل مدیریت بایکود'
admin.site.site_title   = 'بایکود'
admin.site.index_title  = 'داشبورد مدیریت'

# ── Custom dashboard stats injected into admin index page ──
original_index = admin.site.index


def custom_index(request, extra_context=None):
    from shop.models import Product, Order
    from blog.models import Post
    from core.models import ContactMessage

    extra_context = extra_context or {}

    orders = Order.objects.all()
    active_orders = orders.exclude(status='cancelled')

    extra_context.update({
        'total_orders':       orders.count(),
        'pending_orders':     orders.filter(status='pending').count(),
        'total_revenue':      sum(o.total_price for o in active_orders),
        'total_products':     Product.objects.count(),
        'low_stock_products': Product.objects.filter(stock__gt=0, stock__lte=5, is_available=True),
        'out_of_stock_count': Product.objects.filter(stock=0).count(),
        'total_posts':        Post.objects.filter(is_published=True).count(),
        'unread_messages':    ContactMessage.objects.filter(is_read=False).count(),
        'recent_orders':      orders.order_by('-created_at')[:5],
    })

    return original_index(request, extra_context)


admin.site.index = custom_index