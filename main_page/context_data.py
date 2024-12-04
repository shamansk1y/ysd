from accounts.models import Favorite
from django.db.models import Count
from blog.models import Blog
from store.models import Manufacturer
from category.models import Category
from .forms import ContactUsForm, SubscriptionForm
from .models import Contacts, Hero, Baner, Payment, Delivery
from store.models import Product, RecommendedProduct

def get_common_context():
    return {
        'slider': Hero.objects.filter(is_visible=True).order_by('position'),
        'contacts': Contacts.objects.get(id=1),
        'subscription': SubscriptionForm(),
        'contact_us': ContactUsForm(),
        'last_products': Product.objects.order_by('-created')[:8],
        'categories': Category.objects.filter(is_visible=True).order_by('position'),
        'baner': Baner.objects.get(id=1),
        'last_post': Blog.objects.order_by('-pub_date')[:4],
        'main_page_categories': Category.objects.filter(is_visible=True).order_by('position')[:6],
        'brands': Manufacturer.objects.filter(is_visible=True),
        'manufacturers': Manufacturer.objects.filter(is_visible=True),
        'payment': Payment.objects.get(id=1),
        'delivery': Delivery.objects.get(id=1),
        'recommended_products': RecommendedProduct.objects.all()[:8],
    }


def get_page_context(request):
    favorites_count = 0
    if request.user.is_authenticated:
        favorites_count = Favorite.objects.filter(user=request.user).aggregate(count=Count('id'))['count']


    data = {
        # 'user_manager': request.user.groups.filter(name='manager').exists(),
        'user_auth': request.user.is_authenticated,
        'favorites_count': favorites_count,
    }
    context = get_common_context()
    data.update(context)
    return data
