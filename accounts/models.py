from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone   = models.CharField(max_length=20, blank=True, verbose_name='شماره تلفن')
    address = models.TextField(blank=True, verbose_name='آدرس')
    avatar  = models.ImageField(upload_to='avatars/', blank=True, verbose_name='تصویر پروفایل')

    class Meta:
        verbose_name        = 'پروفایل'
        verbose_name_plural = 'پروفایل‌ها'

    def __str__(self):
        return f'پروفایل {self.user.username}'