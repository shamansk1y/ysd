import os
from io import BytesIO
from ckeditor.fields import RichTextField
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from store.utils import get_file_name
from category.models import Category
from PIL import Image


class Manufacturer(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to=get_file_name)
    grid_image = models.ImageField(upload_to=get_file_name, blank=True)
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    description = RichTextField()
    h1 = models.CharField(max_length=255, blank=True)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # проверяем, есть ли изображение
        if self.image:
            # открываем изображение с помощью библиотеки PIL
            img = Image.open(self.image)

            # проверяем, является ли изображение квадратным
            if img.width != img.height:
                size = (max(img.width, img.height), max(img.width, img.height))
                img_with_border = Image.new("RGB", size, (245, 245, 245))
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                img_with_border.paste(img, (x, y))

                # получаем формат изображения из имени файла
                file_ext = os.path.splitext(self.image.name)[1].lower()
                format_dict = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF'}
                image_format = format_dict.get(file_ext, 'JPEG')

                # сохраняем квадратное изображение в том же формате, что и оригинал
                img_io = BytesIO()
                img_with_border.save(img_io, format=image_format)
                img_io.seek(0)
                self.image.save(self.image.name, ContentFile(img_io.read()), save=False)

        super(Manufacturer, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("store:brand_detail", args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to=get_file_name, blank=True)
    article = models.CharField(max_length=200, null=True, blank=True)
    barcode = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)
    description = models.TextField(blank=True)
    main_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    product_count = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    bags_in_case = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_quantity = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    available = models.BooleanField(default=True)
    position = models.PositiveIntegerField(default=1)
    category = models.ManyToManyField(Category, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STASTUS_CHOICES = [
        ('N', 'Out of Stock'),
        ('I', 'In stock'),
        ('S', 'Soon in stock'),
        ]
    status = models.CharField(max_length=1, choices=STASTUS_CHOICES, blank=True, default='N')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def price(self):
        if self.discounted_price is None or self.discounted_price >= self.main_price:
            return self.main_price
        else:
            return self.discounted_price

    def save(self, *args, **kwargs):
        if self.image:
            # открываем изображение с помощью библиотеки PIL
            img = Image.open(self.image)

            # проверяем, является ли изображение квадратным
            if img.width != img.height:
                size = (max(img.width, img.height), max(img.width, img.height))
                img_with_border = Image.new("RGB", size, (255, 255, 255))
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                img_with_border.paste(img, (x, y))

                # получаем формат изображения из имени файла
                file_ext = os.path.splitext(self.image.name)[1].lower()
                format_dict = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF'}
                image_format = format_dict.get(file_ext, 'JPEG')

                # сохраняем квадратное изображение в том же формате, что и оригинал
                img_io = BytesIO()
                img_with_border.save(img_io, format=image_format)
                img_io.seek(0)
                self.image.save(self.image.name, ContentFile(img_io.read()), save=False)

        super(Product, self).save(*args, **kwargs)




class Promo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_file_name, blank=True)
    products = models.ManyToManyField(Product, related_name='promos')
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('store:promo_detail', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Promo'
        verbose_name_plural = 'Promos'


class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Recommended products'

    def __str__(self):
        return self.product.name
