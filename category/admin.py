from django.contrib import admin
from .models import Category
from store.models import Product


# Встраиваем товары в админку категории
class ProductInline(admin.TabularInline):
    model = Product.category.through  # Используем правильную модель связи ManyToMany
    extra = 0  # Убираем лишние пустые строки
    fields = ['product']  # Отображаем только поле 'product'
    verbose_name = 'Product'
    verbose_name_plural = 'Products'
    can_delete = True  # Разрешаем удаление товаров

    # Запрещаем добавление новых товаров
    def has_add_permission(self, request, obj=None):
        return False

    # Запрещаем редактирование товаров
    def has_change_permission(self, request, obj=None):
        return False

    # Разрешаем просмотр товаров
    def has_view_permission(self, request, obj=None):
        return True

    # Разрешаем удаление товаров
    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductInline]  # Включаем в админку встраивание товаров
