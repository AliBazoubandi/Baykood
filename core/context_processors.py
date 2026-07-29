SITE_CONFIG = {
    'site_name': 'بایکود',
    'site_name_en': 'Baykood',
    'site_slogan': 'طبیعت در خدمت شما',
    'phone_number': '09123456789',  # will change this later its just for testing
    'telegram_url': 'https://t.me/erling',  # will change this later its just for testing
    'whatsapp_number': '09123456789',  # will change this later its just for testing
    'instagram_url': 'https://www.instagram.com/erling',    # will change this later its just for testing
    'youtube_url': 'https://www.youtube.com/@Fireship',      # will change this later its just for testing
}

def site_config(request):
    return {'site': SITE_CONFIG}

def cart_count(request):
    cart = request.session.get('cart', {})
    count = sum(cart.values())
    return {'cart_count': count if count > 0 else None}