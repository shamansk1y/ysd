from django.urls import path, include
from .views import home, contacts, about, payment, delivery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('payment/', payment, name='payment'),
    path('delivery/', delivery, name='delivery'),
    # path('opt/', opt, name='opt'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
