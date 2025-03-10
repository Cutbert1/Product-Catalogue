# Generated by Django 4.2.19 on 2025-02-27 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_products_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={
                'ordering': ['-created_on'], 'verbose_name':
                'Product', 'verbose_name_plural': 'Products'
                },
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(
                default=datetime.date.today, verbose_name='Creation Date'
                ),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(
                auto_now=True, verbose_name='Last Updated Date'
                ),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(
                upload_to='products/', verbose_name='Product Image'
                ),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(
                max_length=255, verbose_name='Product Name'
                ),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name='Product Price'
                ),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
