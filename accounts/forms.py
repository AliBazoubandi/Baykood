from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    email      = forms.EmailField(required=True, label='ایمیل')
    first_name = forms.CharField(max_length=50, required=False, label='نام')
    last_name  = forms.CharField(max_length=50, required=False, label='نام خانوادگی')

    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'نام کاربری',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition'
            })
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تکرار رمز عبور'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition'
            })
        self.fields['username'].label = 'نام کاربری'
        self.fields['password'].label = 'رمز عبور'


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False, label='نام')
    last_name  = forms.CharField(max_length=50, required=False, label='نام خانوادگی')
    email      = forms.EmailField(required=False, label='ایمیل')

    class Meta:
        model  = Profile
        fields = ['phone', 'address', 'avatar']
        labels = {
            'phone':   'شماره تلفن',
            'address': 'آدرس',
            'avatar':  'تصویر پروفایل',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full bg-earth-50 border border-earth-200 rounded-xl px-4 py-3 text-earth-800 text-sm focus:outline-none focus:border-earth-500 focus:ring-1 focus:ring-earth-400 transition'
            })