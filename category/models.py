from django.db import models
from django.utils.text import slugify
from york_site.utils import get_file_name
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image
import os
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Slug')
    photo = models.ImageField(upload_to=get_file_name, verbose_name='Image', blank=True, null=True)
    position = models.PositiveIntegerField(default=0, verbose_name='Position')
    description = models.CharField(max_length=255)
    is_visible = models.BooleanField(default=True, verbose_name='Visible')
    category_main_page = models.BooleanField(default=False, verbose_name='Visible on main page')
    meta_title = models.CharField(max_length=255, verbose_name='Meta-teg Title', blank=True)
    meta_description = models.CharField(max_length=255, verbose_name='Meta-teg Description', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if self.photo:
            img = Image.open(self.photo)
            if img.width != img.height:
                size = (max(img.width, img.height), max(img.width, img.height))
                img_with_border = Image.new("RGB", size, (128, 128, 128))
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                img_with_border.paste(img, (x, y))
                file_ext = os.path.splitext(self.photo.name)[1].lower()
                format_dict = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF'}
                image_format = format_dict.get(file_ext, 'JPEG')
                img_io = BytesIO()
                img_with_border.save(img_io, format=image_format)
                img_io.seek(0)
                new_filename = f"{self.slug}{file_ext}"
                self.photo.save(new_filename, ContentFile(img_io.read()), save=False)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['position'] 
        verbose_name = 'Category'
        verbose_name_plural = 'Сategories'

    def get_absolute_url(self):
        return reverse("product_list", args=[self.slug])
