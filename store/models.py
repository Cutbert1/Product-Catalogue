from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(verbose_name="Product Description")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Product Price"
        )
    image = models.ImageField(
        upload_to='products/', verbose_name="Product Image"
        )
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation Date"
        )
    updated_on = models.DateTimeField(
        auto_now=True, verbose_name="Last Updated Date"
        )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Review(models.Model):
    post = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviewer'
    )
    body = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
