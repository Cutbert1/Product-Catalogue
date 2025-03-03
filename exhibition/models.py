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
