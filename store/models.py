from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)

    def fetch_all_categories(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    def get_all_product():
        return Product.objects.all()

    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product()
