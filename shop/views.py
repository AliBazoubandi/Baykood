from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Category


# ─── helpers ──────────────────────────────────────────────
def get_cart(request):
    return request.session.get('cart', {})

def save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True


# ─── product list ─────────────────────────────────────────
def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products   = Product.objects.filter(is_available=True)
    current_category = None

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/product_list.html', {
        'products':         products,
        'categories':       categories,
        'current_category': current_category,
    })


# ─── product detail ───────────────────────────────────────
def product_detail(request, slug):
    product        = get_object_or_404(Product, slug=slug, is_available=True)
    gallery_images = product.images.all()
    related        = Product.objects.filter(
        category=product.category, is_available=True
    ).exclude(id=product.id)[:4]

    return render(request, 'shop/product_detail.html', {
        'product':        product,
        'gallery_images': gallery_images,
        'related':        related,
    })


# ─── cart ─────────────────────────────────────────────────
def cart_detail(request):
    cart     = get_cart(request)
    items    = []
    total    = 0

    for product_id, qty in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            subtotal = product.price * qty
            total   += subtotal
            items.append({
                'product':  product,
                'quantity': qty,
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            pass

    return render(request, 'shop/cart.html', {
        'cart_items': items,
        'total':      total,
    })


def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    cart    = get_cart(request)
    key     = str(product_id)
    qty     = int(request.POST.get('quantity', 1))

    if key in cart:
        cart[key] = min(cart[key] + qty, product.stock)
    else:
        cart[key] = min(qty, product.stock)

    save_cart(request, cart)
    messages.success(request, f'«{product.name}» به سبد خرید اضافه شد.')
    return redirect('shop:cart_detail')


def cart_remove(request, product_id):
    cart = get_cart(request)
    cart.pop(str(product_id), None)
    save_cart(request, cart)
    return redirect('shop:cart_detail')

from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from .models import Order, OrderItem


def checkout(request):
    cart  = get_cart(request)

    # redirect to shop if cart is empty
    if not cart:
        messages.warning(request, 'سبد خرید شما خالی است.')
        return redirect('shop:product_list')

    # build cart items for display
    items = []
    total = 0
    for product_id, qty in cart.items():
        try:
            product  = Product.objects.get(id=int(product_id), is_available=True)
            subtotal = product.price * qty
            total   += subtotal
            items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
        except Product.DoesNotExist:
            pass

    # pre-fill form from user profile if logged in
    initial = {}
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        initial = {
            'full_name': request.user.get_full_name(),
            'phone':     profile.phone if profile else '',
            'address':   profile.address if profile else '',
        }

    form = CheckoutForm(request.POST or None, initial=initial)

    if request.method == 'POST' and form.is_valid():
        # create the order
        order = Order.objects.create(
            user        = request.user if request.user.is_authenticated else None,
            full_name   = form.cleaned_data['full_name'],
            phone       = form.cleaned_data['phone'],
            address     = form.cleaned_data['address'],
            note        = form.cleaned_data.get('note', ''),
            total_price = total,
        )

        # create order items and reduce stock
        for item in items:
            OrderItem.objects.create(
                order    = order,
                product  = item['product'],
                quantity = item['quantity'],
                price    = item['product'].price,
            )
            item['product'].stock = max(0, item['product'].stock - item['quantity'])
            item['product'].save()

        # clear the cart
        request.session['cart'] = {}
        request.session.modified = True

        messages.success(request, f'سفارش شما با موفقیت ثبت شد. شماره سفارش: #{order.id}')
        return redirect('shop:order_confirmation', order_id=order.id)

    return render(request, 'shop/checkout.html', {
        'form':  form,
        'items': items,
        'total': total,
    })


def order_confirmation(request, order_id):
    order = Order.objects.prefetch_related('items__product').get(id=order_id)
    return render(request, 'shop/order_confirmation.html', {'order': order})