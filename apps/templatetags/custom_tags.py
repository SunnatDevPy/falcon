import datetime
from datetime import timedelta

from django.template import Library

from apps.models import LoveProduct

register = Library()


@register.filter(name='is_love')
def is_love(product_id, user_id):
    return LoveProduct.objects.filter(user_id=user_id, product_id=product_id)

@register.filter(name='change_phone')
def change_phone(phone):
    return phone[4:].replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
