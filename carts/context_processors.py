from .models import Cart, CartItem
from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist

def cart_details(request):
    total = 0
    quantity = 0
    cart_items = []
    tax = 0
    grand_total = 0
    product_ids_in_cart = []

    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price() * cart_item.quantity)
            quantity += cart_item.quantity
            product_ids_in_cart.append(cart_item.product.id)

        tax = (2 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        # Return default values if no cart exists
        cart_items = []
        total = 0
        quantity = 0

    return {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        'product_ids_in_cart': product_ids_in_cart,
    }
