SITE_CONFIG = {
    'site_name': 'کشاورزی سبز',
    'site_name_en': 'Agrishop',
    'site_slogan': 'طبیعت در خدمت شما',
    'telegram_url': 'https://t.me/YOUR_TELEGRAM_USERNAME',
    'whatsapp_number': '',  # add later if needed
    'instagram_url': '',    # add later if needed
    'youtube_url': '',      # add later if needed
}

def site_config(request):
    return {'site': SITE_CONFIG}

def cart_count(request):
    cart = request.session.get('cart', {})
    count = sum(cart.values())
    return {'cart_count': count if count > 0 else None}