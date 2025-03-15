from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Product(models.Model):
    """
    Stores information about individual product. Also tracks the
    product's creation and update times and
    its current status related to :model: `auth.User`

    Meta:
        verbose_name (str): Single instance of the model, human readable name
        ordering (list): Ordering for querysets (newest products first).

    Methods:
        __str__: Returns a string representation of the product.
    """

    name = models.CharField(
        max_length=255, unique=True, verbose_name="Product Name"
        )
    slug = models.SlugField(max_length=255, unique=True, null=True)
    marketer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,
        related_name="store_products", verbose_name="Marketer"
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
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Review(models.Model):
    """
    Stores information on reviews submitted by users an
    individaul product related to
    :model: `auth.User` and :model: `store.Product`

    Meta:
        ordering: Review creation date in descending order.
        verbose_name: Name for model in admin interface.
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='reviews'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='reviewer'
    )
    body = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'

    def __str__(self):
        return f'Review by {self.author} on {self.product}'
