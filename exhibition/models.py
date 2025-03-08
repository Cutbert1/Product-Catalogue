from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Exhibition(models.Model):
    STATUS_CHOICES = [
        (0, 'Draft'),
        (1, 'Scheduled'),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='exhibition/', verbose_name="Exhibition Image") # noqa
    scheduled_status = models.IntegerField(choices=STATUS_CHOICES, default=0)
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
        verbose_name_plural = "Exhibitions"
        ordering = ['start_date']


class ExhibitionRegistration(models.Model):
    MAX_LENGTH_BUSINESS_NAME = 255
    MAX_LENGTH_ADDRESS = 255
    MAX_LENGTH_PRODUCT_DESCRIPTION = 1000

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
        verbose_name_plural = "Exhibition Registrations"
        ordering = ['business_name']
