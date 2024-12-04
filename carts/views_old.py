from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Cart, CartItem
from main_page.context_data import get_common_context, get_page_context

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        request.session.save()
        cart = request.session.session_key
    return cart

def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    current_user = request.user
    if current_user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=current_user, product=product, defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('cart:cart')

def cart(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        if cart_items.exists():
            for cart_item in cart_items:
                cart_item.total_price = cart_item.product.price() * cart_item.quantity
                total += cart_item.total_price
                quantity += cart_item.quantity
            tax = (2 * total) / 100
            grand_total = total + tax
    except ObjectDoesNotExist:
        cart_items = []

    data = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'carts/cart.html', context=data)

def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(user=request.user, product=product, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(cart=cart, product=product, id=cart_item_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:cart')

def add_one_qty(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(user=request.user, product=product)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart')

def remove_cart_item(request, product_id):
    product = get_object_or_404(Product, product=product_id, id=cart_item_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(user=request.user, product=product, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(cart=cart, product=product)

    cart_item.delete()
    return redirect('cart:cart')

def fast_add_to_cart(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug)
    current_user = request.user
    if current_user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=current_user, product=product, defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('store:product_detail', slug=slug)

@login_required(login_url='accounts:login')
def checkout(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        if cart_items.exists():
            for cart_item in cart_items:
                cart_item.total_price = cart_item.product.price() * cart_item.quantity
                total += cart_item.total_price
                quantity += cart_item.quantity
            tax = (2 * total) / 100
            grand_total = total + tax
    except ObjectDoesNotExist:
        cart_items = []

    data = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'carts/checkout.html', context=data)
