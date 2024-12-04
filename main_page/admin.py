from django.contrib import admin
from main_page.models import Contacts, ContactUs, Subscription, Hero, Baner, Payment, Delivery




@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    model = Contacts
    list_editable = [
            'content',
            'address',
            'map_url_address',
            'phone_1',
            'phone_2',
            'phone_3',
            'email',
            'day_open',
            'hours_of_work',
            'weekend_work',
            'weekend_hours_of_work'
            ]
    list_display = [
                'content',
                'map_url_address',
                'address',
                'phone_1',
                'phone_2',
                'phone_3',
                'email',
                'day_open',
                'hours_of_work',
                'weekend_work',
                'weekend_hours_of_work']
    list_display_links = None



@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_editable = ['name', 'email', 'subject', 'message', 'is_processed']
    list_display = ['name', 'email', 'subject', 'message', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_editable = ['email', 'is_processed']
    list_display = ['email', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    model = Hero
    list_editable = ['title', 'position', 'image', 'image_bg', 'is_visible', 'h_1', 'desc', 'tab', 'tab_url']
    list_display = ['title', 'position', 'image', 'image_bg','is_visible', 'h_1', 'desc', 'tab', 'tab_url']
    list_display_links = None


@admin.register(Baner)
class BanerAdmin(admin.ModelAdmin):
    model = Baner
    list_editable = ['title', 'position', 'image_1', 'h_1', 'desc_1', 'tab_1', 'tab_url_1','image_2', 'h_2', 'desc_2', 'tab_2', 'tab_url_2']
    list_display = ['title', 'position', 'image_1', 'h_1', 'desc_1', 'tab_1', 'tab_url_1','image_2', 'h_2', 'desc_2', 'tab_2', 'tab_url_2']
    list_display_links = None


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_editable = ['title', 'image', 'content']
    list_display = ['title', 'image', 'content']
    list_display_links = None


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    model = Delivery
    list_editable = ['title', 'image', 'content']
    list_display = ['title', 'image', 'content']
    list_display_links = None
