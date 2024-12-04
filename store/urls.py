from django.urls import path
from .views import product_list, product_detail, category_list, all_product_list, search, brands, brand_detail, promo_list, promo_detail

app_name = 'store'

urlpatterns = [
    path('promo/', promo_list, name='promo_list'),
    path('promo/<slug:slug>/', promo_detail, name='promo_detail'),
    path('brands/', brands, name='brands'),
    path('brands/<slug:slug>/', brand_detail, name='brand_detail'),
    path('search/', search, name='search'),
    path('category/', category_list, name='category_list'),
    path('category/<slug:slug>/', product_list, name='product_list'),
    path('<slug:slug>/', product_detail, name='product_detail'),
    path('', all_product_list, name='all_product_list'),




]
