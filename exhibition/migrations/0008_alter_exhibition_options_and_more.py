# Generated by Django 4.2.19 on 2025-03-14 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0007_remove_exhibitionregistration_user_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exhibition',
            options={'ordering': ['start_date'], 'verbose_name': 'Exhibition'},
        ),
        migrations.AlterModelOptions(
            name='exhibitionregistration',
            options={'ordering': ['business_name'], 'verbose_name': 'Exhibition Registration'},
        ),
    ]
