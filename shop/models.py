from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name        = models.CharField(max_length=200, verbose_name='نام دسته‌بندی')
    slug        = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    description = models.TextField(blank=True, verbose_name='توضیحات')
    image       = models.ImageField(upload_to='categories/', blank=True, verbose_name='تصویر')
    parent      = models.ForeignKey(
        'self', on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='children',
        verbose_name='دسته‌بندی والد'
    )
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering            = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    category    = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='products',
        verbose_name='دسته‌بندی'
    )
    name        = models.CharField(max_length=300, verbose_name='نام محصول')
    slug        = models.SlugField(max_length=300, unique=True, allow_unicode=True)
    description = models.TextField(verbose_name='توضیحات')
    price       = models.PositiveIntegerField(verbose_name='قیمت (تومان)')
    stock       = models.PositiveIntegerField(default=0, verbose_name='موجودی انبار')
    is_available = models.BooleanField(default=True, verbose_name='موجود است')
    is_featured  = models.BooleanField(default=False, verbose_name='محصول ویژه')
    weight      = models.CharField(max_length=50, blank=True, verbose_name='وزن / حجم')
    cover_image = models.ImageField(upload_to='products/', verbose_name='تصویر اصلی')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering            = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def formatted_price(self):
        return f'{self.price:,} تومان'


class ProductImage(models.Model):
    product  = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='images',
        verbose_name='محصول'
    )
    image    = models.ImageField(upload_to='products/gallery/', verbose_name='تصویر')
    alt_text = models.CharField(max_length=200, blank=True, verbose_name='متن جایگزین')

    class Meta:
        verbose_name        = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصول'

    def __str__(self):
        return f'تصویر برای {self.product.name}'
    
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING   = 'pending',   'در انتظار بررسی'
        CONFIRMED = 'confirmed', 'تأیید شده'
        SHIPPED   = 'shipped',   'ارسال شده'
        DELIVERED = 'delivered', 'تحویل داده شده'
        CANCELLED = 'cancelled', 'لغو شده'

    user        = models.ForeignKey(
        'auth.User', on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders',
        verbose_name='کاربر'
    )
    full_name   = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    phone       = models.CharField(max_length=20, verbose_name='شماره تماس')
    address     = models.TextField(verbose_name='آدرس تحویل')
    note        = models.TextField(blank=True, verbose_name='توضیحات سفارش')
    status      = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name='وضعیت'
    )
    total_price = models.PositiveIntegerField(default=0, verbose_name='مبلغ کل (تومان)')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'سفارش'
        verbose_name_plural = 'سفارش‌ها'
        ordering            = ['-created_at']

    def __str__(self):
        return f'سفارش #{self.id} — {self.full_name}'

    def formatted_total(self):
        return f'{self.total_price:,} تومان'


class OrderItem(models.Model):
    order    = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name='items',
        verbose_name='سفارش'
    )
    product  = models.ForeignKey(
        Product, on_delete=models.SET_NULL,
        null=True,
        verbose_name='محصول'
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    price    = models.PositiveIntegerField(verbose_name='قیمت واحد (تومان)')

    class Meta:
        verbose_name        = 'آیتم سفارش'
        verbose_name_plural = 'آیتم‌های سفارش'

    def __str__(self):
        return f'{self.quantity}x {self.product}'

    def subtotal(self):
        if self.price is None or self.quantity is None:
            return 0
        return self.price * self.quantity

    def formatted_subtotal(self):
        return f'{self.subtotal():,} تومان'