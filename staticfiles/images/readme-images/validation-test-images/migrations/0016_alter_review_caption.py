# Generated by Django 4.2.19 on 2025-03-08 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_review_caption_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='caption',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
