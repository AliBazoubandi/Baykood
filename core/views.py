from django.shortcuts import render, redirect
from django.contrib import messages
from shop.models import Product, Category
from blog.models import Post
from .forms import ContactForm


def home(request):
    featured_products  = Product.objects.filter(is_available=True, is_featured=True)[:4]
    featured_categories = Category.objects.filter(show_on_homepage=True)
    recent_posts        = Post.objects.filter(is_published=True)[:3]

    return render(request, 'core/home.html', {
        'featured_products':   featured_products,
        'featured_categories': featured_categories,
        'recent_posts':        recent_posts,
    })


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.')
        return redirect('core:contact')
    return render(request, 'core/contact.html', {'form': form})