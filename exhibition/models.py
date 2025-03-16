from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Exhibition(models.Model):
    """
    Renders information about exhibitions, including their status,
    details, scheduling, and capacity.

    Also includes a string representation and Meta options for
    verbose name and ordering.

    Template: exhibition/exhbition.html
    """
    STATUS_CHOICES = [
        (0, 'Draft'),
        (1, 'Scheduled'),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    scheduled_status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    exhibition_image = CloudinaryField('image', default='placeholder')
    venue = models.CharField(max_length=255)
    max_attendees = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Exhibition"
        ordering = ['start_date']


class ExhibitionRegistration(models.Model):
    """
    Stores information about businesses registering for an exhibition,
    including their contact details and product description.

    Meta:
        verbose_name (str):  Model human-readable name.
        ordering (list): Ordering by registration_date.

    Template: exhibition/exhbition.html
    """
    MAX_LENGTH_BUSINESS_NAME = 255
    MAX_LENGTH_ADDRESS = 255
    MAX_LENGTH_PRODUCT_DESCRIPTION = 1000

    registration_date = models.DateTimeField(
       default=timezone.now, verbose_name="Registration Date")
    business_name = models.CharField(max_length=MAX_LENGTH_BUSINESS_NAME)
    address = models.CharField(max_length=MAX_LENGTH_ADDRESS)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    product_description = models.TextField(
        max_length=MAX_LENGTH_PRODUCT_DESCRIPTION
        )
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Exhibition registration from {self.business_name}"

    class Meta:
        verbose_name = "Exhibition Registration"
        ordering = ['registration_date']
