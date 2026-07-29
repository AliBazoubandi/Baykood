from django import forms


class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=200,
        label='نام و نام خانوادگی',
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
            'placeholder': 'مثال: علی رضایی',
        })
    )
    phone = forms.CharField(
        max_length=20,
        label='شماره تماس',
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
            'placeholder': '09xxxxxxxxx',
        })
    )
    address = forms.CharField(
        label='آدرس کامل تحویل',
        widget=forms.Textarea(attrs={
            'class': 'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
            'rows': 3,
            'placeholder': 'استان، شهر، خیابان، پلاک، کدپستی',
        })
    )
    note = forms.CharField(
        required=False,
        label='توضیحات (اختیاری)',
        widget=forms.Textarea(attrs={
            'class': 'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition',
            'rows': 2,
            'placeholder': 'هر نکته‌ای که باید بدانیم...',
        })
    )