from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage, Order, OrderItem


class ProductImageInline(admin.TabularInline):
    model       = ProductImage
    extra       = 3
    fields      = ['image', 'alt_text', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:6px;" />',
                obj.image.url
            )
        return '—'
    image_preview.short_description = 'پیش‌نمایش'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'icon_preview', 'color', 'show_on_homepage', 'order', 'parent', 'product_count']
    list_filter   = ['show_on_homepage', 'color', 'parent']
    list_editable = ['show_on_homepage', 'order']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'slug', 'description', 'short_description')
        }),
        ('نمایش در صفحه اصلی', {
            'fields': ('icon', 'icon_image', 'color', 'image', 'show_on_homepage', 'order')
        }),
        ('دسته‌بندی والد', {
            'fields': ('parent',)
        }),
    )

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'تعداد محصولات'

    def icon_preview(self, obj):
        if obj.icon_image:
            return format_html('<img src="{}" style="height:28px;" />', obj.icon_image.url)
        return f'lucide: {obj.icon}'
    icon_preview.short_description = 'آیکون'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = [
        'cover_preview', 'name', 'category',
        'formatted_price_display', 'stock', 'is_available', 'is_featured'
    ]
    list_display_links = ['cover_preview', 'name']
    list_filter   = ['is_available', 'is_featured', 'category']
    list_editable = ['is_available', 'is_featured', 'stock']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering      = ['-created_at']
    inlines       = [ProductImageInline]

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('قیمت و موجودی', {
            'fields': ('price', 'stock', 'weight', 'is_available', 'is_featured')
        }),
        ('تصویر اصلی', {
            'fields': ('cover_image',)
        }),
        ('رسانه', {
        'fields': ('cover_image', 'video_url'),
        'description': 'برای افزودن ویدیوی معرفی، لینک YouTube یا Instagram را وارد کنید'
        }),
    )

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="height:48px; width:48px; object-fit:cover; border-radius:8px;" />',
                obj.cover_image.url
            )
        return '—'
    cover_preview.short_description = ''

    def formatted_price_display(self, obj):
        return format_html(
            '<span style="font-weight:600; color:#6e5030;">{}</span>',
            obj.formatted_price()
        )
    formatted_price_display.short_description = 'قیمت'

class OrderItemInline(admin.TabularInline):
    model           = OrderItem
    extra           = 0
    readonly_fields = ['product', 'quantity', 'price', 'get_subtotal']
    can_delete      = False

    def get_subtotal(self, obj):
        if obj.pk is None:
            return '—'
        return obj.formatted_subtotal()
    get_subtotal.short_description = 'جمع'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display        = ['id', 'full_name', 'phone', 'status', 'status_badge', 'formatted_total_display', 'created_at']
    list_editable       = ['status']
    list_filter         = ['status', 'created_at']
    list_editable       = ['status']
    search_fields       = ['full_name', 'phone', 'address']
    readonly_fields     = ['user', 'total_price', 'created_at']
    ordering            = ['-created_at']
    inlines             = [OrderItemInline]

    fieldsets = (
        ('اطلاعات مشتری', {
            'fields': ('user', 'full_name', 'phone', 'address', 'note')
        }),
        ('وضعیت سفارش', {
            'fields': ('status', 'total_price', 'created_at')
        }),
    )

    def status_badge(self, obj):
        colors = {
            'pending':   '#b08a56',
            'confirmed': '#2563eb',
            'shipped':   '#7c3aed',
            'delivered': '#16a34a',
            'cancelled': '#dc2626',
        }
        color = colors.get(obj.status, '#888')
        return format_html(
            '<span style="background:{}; color:white; padding:3px 10px; border-radius:20px; font-size:12px; font-weight:600;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'وضعیت'

    def formatted_total_display(self, obj):
        return obj.formatted_total()
    formatted_total_display.short_description = 'مبلغ کل'