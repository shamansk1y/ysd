# Generated by Django 4.2.4 on 2024-10-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_manufacturer_options_promo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_count',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
