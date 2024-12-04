from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', views.profile, name='profile'),

    path('favorite_add/<slug:slug>/', views.add_to_favorite, name='add_to_favorite'),
    path('favorite_remove/<slug:slug>/', views.remove_from_favorite, name='remove_from_favorite'),
    path('favorite_remove-detail/<slug:slug>/', views.remove_from_favorite_detail, name='remove_from_favorite_detail'),
    path('favorite/', views.favorite_list, name='favorite_list'),


    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),

    path('my_orders/', views.my_orders, name='my_orders'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('change_password/', views.change_password, name='change_password'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),

]
