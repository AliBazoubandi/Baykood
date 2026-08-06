import jdatetime
from django import template

register = template.Library()

PERSIAN_MONTHS = [
    'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
    'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'
]

PERSIAN_DIGITS = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')


@register.filter
def to_jalali(value, fmt='numeric'):
    """
    Converts a Gregorian datetime to a Persian (Jalali) date string.
    Usage:
      {{ order.created_at|to_jalali }}          → ۱۴۰۴/۱۰/۲۵
      {{ post.published_at|to_jalali:"long" }}  → ۲۵ دی ۱۴۰۴
    """
    if not value:
        return ''

    j = jdatetime.date.fromgregorian(date=value.date() if hasattr(value, 'date') else value)

    if fmt == 'long':
        result = f'{j.day} {PERSIAN_MONTHS[j.month - 1]} {j.year}'
    else:
        result = f'{j.year}/{j.month:02d}/{j.day:02d}'

    return result.translate(PERSIAN_DIGITS)