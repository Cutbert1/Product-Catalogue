from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Product(models.Model):

    name = models.CharField(
        max_length=255, unique=True, verbose_name="Product Name" # noqa
        )
    slug = models.SlugField(max_length=255, unique=True, null=True)
    marketer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="Marketer"
        )
    products_image = CloudinaryField("image", default="placeholder")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Product Price"
        )
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation Date"
        )
    status = models.IntegerField(choices=STATUS, default=0)
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
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='reviews'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='reviewer'
    )
    body = models.TextField()
    image = models.ImageField(
        default="review_default.jpg", upload_to="reviews/", null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'Review by {self.author} on {self.product}'
