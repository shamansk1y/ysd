from django.contrib import admin
from django import forms
from store.models import Manufacturer, Product, Promo, RecommendedProduct
from django.contrib.admin.widgets import FilteredSelectMultiple


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    prepopulated_fields = {'slug': ('title',)}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': FilteredSelectMultiple('Categories', is_stacked=False),  # Добавляем кастомный виджет
        }


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm  # Указываем, что используется кастомная форма
    list_display = ['name', 'image', 'main_price', 'available', 'manufacturer', 'category_display', 'status']
    list_filter = ['available', 'manufacturer', 'category', 'status', 'created', 'updated']
    list_editable = ['image', 'main_price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    # Этот метод отображает выбранные категории для товара
    def category_display(self, obj):
        return ", ".join([category.name for category in obj.category.all()])
    category_display.short_description = 'Categories'


admin.site.register(Product, ProductAdmin)


class PromoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    filter_horizontal = ('products',)  # Этот параметр поможет управлять ManyToMany полем для продуктов

admin.site.register(Promo, PromoAdmin)


@admin.register(RecommendedProduct)
class RecommendedProduct(admin.ModelAdmin):
    model = RecommendedProduct
    list_filter = ['position']
