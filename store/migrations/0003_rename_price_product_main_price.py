# Generated by Django 4.2.4 on 2024-07-14 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_manufacturer_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='main_price',
        ),
    ]
