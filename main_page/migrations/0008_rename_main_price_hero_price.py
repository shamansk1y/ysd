# Generated by Django 4.2.4 on 2024-07-14 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_remove_hero_price_hero_main_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='main_price',
            new_name='price',
        ),
    ]
