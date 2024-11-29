from django.conf import settings
from django import template

register = template.Library()

@register.filter(name='has_img')
def has_image(string):
    if not string:
        string = 'product_images/default.png'
    return f'{settings.MEDIA_URL}{string}'