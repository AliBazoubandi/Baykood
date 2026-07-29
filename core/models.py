from django.db import models


class ContactMessage(models.Model):
    full_name  = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    phone      = models.CharField(max_length=20, verbose_name='شماره تماس')
    email      = models.EmailField(blank=True, verbose_name='ایمیل')
    subject    = models.CharField(max_length=300, verbose_name='موضوع')
    message    = models.TextField(verbose_name='پیام')
    is_read    = models.BooleanField(default=False, verbose_name='خوانده شده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        verbose_name        = 'پیام تماس'
        verbose_name_plural = 'پیام‌های تماس'
        ordering            = ['-created_at']

    def __str__(self):
        return f'{self.full_name} — {self.subject}'