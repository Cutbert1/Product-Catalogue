# Generated by Django 4.2.19 on 2025-03-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_rename_post_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='caption',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(default='review_default.jpg', null=True, upload_to='reviews/'),
        ),
    ]
