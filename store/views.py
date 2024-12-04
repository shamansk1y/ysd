from django.shortcuts import get_object_or_404, render, redirect
from main_page.context_data import get_common_context, get_page_context
from main_page.views import handle_post_request
from .models import Product, Manufacturer, Promo
from category.models import Category
from carts.models import CartItem, Cart
from carts.views import _cart_id
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from accounts.models import Favorite
from decimal import Decimal




def product_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)

    # Получаем уникальные значения только для текущей категории
    weights = products.values_list('weight', flat=True).distinct().order_by('weight')
    bags_in_case = products.values_list('bags_in_case', flat=True).distinct().order_by('bags_in_case')
    manufacturers_cat = Manufacturer.objects.filter(product__category=category).distinct()

    manufacturer_filter = request.GET.get('manufacturer', '')
    weight_filter = request.GET.get('weight', '')
    bags_filter = request.GET.get('bags', '')

    # Обрабатываем manufacturer_filter как строку с разделением по запятым
    manufacturer_filters = []
    if manufacturer_filter:
        manufacturer_filters = [int(m) for m in manufacturer_filter.split(',')]
        products = products.filter(manufacturer__id__in=manufacturer_filters)

    # Обрабатываем weight_filter
    weight_filters = []
    if weight_filter:
        weight_filters = [Decimal(w) for w in weight_filter.split(',')]
        products = products.filter(weight__in=weight_filters)

    # Обрабатываем bags_filter
    bags_filters = []
    if bags_filter:
        bags_filters = [int(b) for b in bags_filter.split(',')]
        products = products.filter(bags_in_case__in=bags_filters)

    data = {
        'page_products': products,
        'category': category,
        'manufacturers_cat': manufacturers_cat,
        'manufacturer_filters': manufacturer_filters,
        'weight_filters': weight_filters,
        'bags_filters': bags_filters,
        'weights': weights,
        'bags_in_case': bags_in_case,
    }

    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)

    return render(request, 'product_list.html', context=data)



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_id = _cart_id(request)
    item_in_cart = False
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user)
    else:
        favorites = None
    user_favorites = []
    if request.user.is_authenticated:
        user_favorites = Favorite.objects.filter(user=request.user, product=product)

    try:
        cart = Cart.objects.get(cart_id=cart_id)
        item_in_cart = CartItem.objects.filter(product=product, cart=cart).exists()
    except Cart.DoesNotExist:
        cart = None

    discount_amount = None
    discount_percentage = None
    # Calculate discount and percentage
    if product.discounted_price is not None:
        discount_amount = product.main_price - product.discounted_price
        discount_percentage = round((discount_amount / product.main_price) * 100, 2)

    # Get similar items, check if category exists
    if product.category.exists():  # Убедитесь, что категория существует
        category = product.category.first()  # Получаем первую категорию (если их несколько)
        similar_items = Product.objects.filter(category=category).exclude(id=product.id)
        similar_items_count = similar_items.count()

        # If less than 4 items, take all, otherwise select 4 random
        if similar_items_count < 4:
            similar_items = similar_items
        else:
            similar_items = similar_items.order_by('?')[:4]
    else:
        similar_items = []  # Если категории нет, просто не показывать похожие товары

    context = {
        'product': product,
        'item_in_cart': item_in_cart,
        'discount_amount': discount_amount,
        'discount_percentage': discount_percentage,
        'similar_items': similar_items,
        'favorites': favorites,
        'user_favorites': user_favorites,

    }

    if request.method == 'POST':
        if not cart:
            cart = Cart.objects.create(cart_id=cart_id)

        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        return redirect('store:product_detail', slug=slug)

    context_req = get_page_context(request)
    context_data = get_common_context()
    context.update(context_data)
    context.update(context_req)
    return render(request, 'details.html', context=context)


def category_list(request):
    if request.method == 'POST':
        handle_post_request(request)

    categories = Category.objects.all()
    data = {
        'categories': categories,
    }
    return render(request, 'category_list.html', context=data)


def all_product_list(request):
    products = Product.objects.filter(available=True).order_by('position')

    # Получаем уникальные значения только для текущей категории
    weights = products.values_list('weight', flat=True).distinct().order_by('weight')
    bags_in_case = products.values_list('bags_in_case', flat=True).distinct().order_by('bags_in_case')
    manufacturers_cat = Manufacturer.objects.filter(is_visible=True).distinct()

    manufacturer_filter = request.GET.get('manufacturer', '')
    weight_filter = request.GET.get('weight', '')
    bags_filter = request.GET.get('bags', '')

    # Обрабатываем manufacturer_filter как строку с разделением по запятым
    manufacturer_filters = []
    if manufacturer_filter:
        manufacturer_filters = [int(m) for m in manufacturer_filter.split(',')]
        products = products.filter(manufacturer__id__in=manufacturer_filters)

    # Обрабатываем weight_filter
    weight_filters = []
    if weight_filter:
        weight_filters = [Decimal(w) for w in weight_filter.split(',')]
        products = products.filter(weight__in=weight_filters)

    # Обрабатываем bags_filter
    bags_filters = []
    if bags_filter:
        bags_filters = [int(b) for b in bags_filter.split(',')]
        products = products.filter(bags_in_case__in=bags_filters)

    data = {
        'page_products': products,
        'manufacturers_cat': manufacturers_cat,
        'manufacturer_filters': manufacturer_filters,
        'weight_filters': weight_filters,
        'bags_filters': bags_filters,
        'weights': weights,
        'bags_in_case': bags_in_case,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'product_list.html', context=data)


def search(request):
    products = []
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword))

    data = {
        'page_products': products,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'search_product_list.html', context=data)


def brands(request):
    brands = Manufacturer.objects.filter(is_visible=True)
    data = {
        'brands': brands,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'store/brands.html', context=data)


def brand_detail(request, slug):
    brand = get_object_or_404(Manufacturer, slug=slug)
    context = {
        'brand': brand,
    }

    context_req = get_page_context(request)
    context_data = get_common_context()
    context.update(context_data)
    context.update(context_req)
    return render(request, 'store/brand_single.html', context=context)


def promo_list(request):
    promos = Promo.objects.filter(is_visible=True)
    context = {
        'promos': promos,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    context.update(context_data)
    context.update(context_req)
    return render(request, 'store/promo_list.html', context=context)


def promo_detail(request, slug):
    promo = get_object_or_404(Promo, slug=slug)
    products = promo.products.all()
    context = {
        'products': products,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    context.update(context_data)
    context.update(context_req)
    return render(request, 'store/promo_detail.html', context=context)
