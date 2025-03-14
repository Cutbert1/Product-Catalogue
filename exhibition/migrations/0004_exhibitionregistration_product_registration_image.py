# Generated by Django 4.2.19 on 2025-03-12 12:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0003_remove_exhibition_image_exhibition_exhibition_image_and_more'), # noqa
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitionregistration',
            name='product_registration_image',
            field=cloudinary.models.CloudinaryField(
                default='placeholder', max_length=255, verbose_name='image'
                ),
        ),
    ]
