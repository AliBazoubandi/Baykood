from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model  = ContactMessage
        fields = ['full_name', 'phone', 'email', 'subject', 'message']
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'phone':     'شماره تماس',
            'email':     'ایمیل (اختیاری)',
            'subject':   'موضوع',
            'message':   'پیام شما',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class':       'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
                'placeholder': 'مثال: علی رضایی',
            }),
            'phone': forms.TextInput(attrs={
                'class':       'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
                'placeholder': '09xxxxxxxxx',
            }),
            'email': forms.EmailInput(attrs={
                'class':       'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
                'placeholder': 'example@email.com',
            }),
            'subject': forms.TextInput(attrs={
                'class':       'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
                'placeholder': 'مثال: سوال درباره محصول',
            }),
            'message': forms.Textarea(attrs={
                'class':       'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
                'rows':        5,
                'placeholder': 'پیام خود را اینجا بنویسید...',
            }),
        }