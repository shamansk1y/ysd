# Generated by Django 5.0.6 on 2024-06-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_contacts_map_url_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='map_url_address',
            field=models.CharField(blank=True, max_length=300, verbose_name='Посилання на google map'),
        ),
    ]
