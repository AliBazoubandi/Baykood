from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'phone', 'subject', 'is_read', 'created_at']
    list_filter   = ['is_read', 'created_at']
    list_editable = ['is_read']
    search_fields = ['full_name', 'phone', 'email', 'subject']
    readonly_fields = ['full_name', 'phone', 'email', 'subject', 'message', 'created_at']
    ordering      = ['-created_at']

    fieldsets = (
        ('اطلاعات فرستنده', {
            'fields': ('full_name', 'phone', 'email', 'created_at')
        }),
        ('پیام', {
            'fields': ('subject', 'message')
        }),
        ('وضعیت', {
            'fields': ('is_read',)
        }),
    )