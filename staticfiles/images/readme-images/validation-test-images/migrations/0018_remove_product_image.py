# Generated by Django 4.2.19 on 2025-03-10 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_review_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
