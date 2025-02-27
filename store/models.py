from django.db import models
from datetime import date


# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(verbose_name="Product Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product Price") # noqa
    image = models.ImageField(upload_to='products/', verbose_name="Product Image") # noqa
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date") # noqa
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Last Updated Date") # noqa

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
