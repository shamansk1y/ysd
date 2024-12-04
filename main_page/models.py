from django.db import models
from ckeditor.fields import RichTextField
from york_site.utils import get_file_name_id


class Hero(models.Model):

    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(verbose_name="Позиція")
    image = models.ImageField(upload_to=get_file_name_id, verbose_name="Image")
    image_bg = models.ImageField(upload_to=get_file_name_id, verbose_name="Фонове зображення")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок")
    desc = models.TextField(max_length=500, blank=True, verbose_name="Опис")
    tab = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки")
    tab_url = models.URLField(blank=True, verbose_name="Посилання з кнопки")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Slider'

class Baner(models.Model):
    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(verbose_name="Позиція")
    image_1 = models.ImageField(upload_to=get_file_name_id, verbose_name="Зображення банер 1")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок банер 1")
    desc_1 = models.TextField(max_length=500, blank=True, verbose_name="Опис банер 1")
    tab_1 = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки банер 1")
    tab_url_1 = models.URLField(blank=True, verbose_name="Посилання з кнопки банер 1")
    image_2 = models.ImageField(upload_to=get_file_name_id, verbose_name="Зображення банер 2")
    h_2 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок банер 2")
    desc_2 = models.TextField(max_length=500, blank=True, verbose_name="Опис банер 2")
    tab_2 = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки банер 2")
    tab_url_2 = models.URLField(blank=True, verbose_name="Посилання з кнопки банер 2")


    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Baner'


class Contacts(models.Model):
    content = RichTextField(blank=True, null=True)
    address = models.CharField(max_length=70, verbose_name="Адреса")
    map_url_address = models.CharField(max_length=300, blank=True, verbose_name="Посилання на google map")
    phone_1 = models.CharField(blank=True, max_length=50, verbose_name="Телефон 1")
    phone_2 = models.CharField(blank=True, max_length=50, verbose_name="Телефон 2")
    phone_3 = models.CharField(blank=True, max_length=50, verbose_name="Телефон 3")
    email = models.CharField(max_length=50, verbose_name="Пошта ")
    day_open = models.CharField(blank=True, max_length=50, verbose_name="Робочі дні")
    hours_of_work = models.CharField(blank=True, max_length=50, verbose_name="Робочі години")
    weekend_work = models.CharField(blank=True, max_length=50, verbose_name="Робота в вихідні")
    weekend_hours_of_work = models.CharField(blank=True, max_length=50, verbose_name="Робочі години в вихідні")

    def __str__(self):
        return f'{self.address}'

    class Meta:
        ordering = ('address',)
        verbose_name_plural = 'Contacts'



class ContactUs(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=250, blank=True)
    subject = models.CharField(max_length=50)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Gateway link"


class Subscription(models.Model):

    email = models.EmailField()
    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Subscribe to email'



class Delivery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=get_file_name_id, verbose_name="Image")
    content = RichTextField(blank=True, null=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Delivery'


class Payment(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=get_file_name_id, verbose_name="Image")
    content = RichTextField(blank=True, null=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Payment'
