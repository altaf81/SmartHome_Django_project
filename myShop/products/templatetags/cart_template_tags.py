from django import template
from products.models import Cart

register = template.Library()


@register.filter
def cart_product_count(user):
    if user.is_authenticated:
        qs = Cart.objects.filter(user=user)
        if qs.exists():
            return qs[0].itemlist.count()
    return 0
