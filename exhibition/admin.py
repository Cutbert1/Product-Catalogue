from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Exhibition, ExhibitionRegistration


# Register your models here.


@admin.register(Exhibition)
class ExhibitionAdmin(SummernoteModelAdmin):
    """
    Admin interface for management of Exhibition objects.
    Provides enhanced display, search, and filtering capabilities.
    SummernoteModelAdmin attribute used to provide rich text editing
    for 'description' field.

    """

    list_display = (
        'title', 'start_date', 'end_date', 'scheduled_status', 'created_on',
        'max_attendees')
    search_fields = ['title', 'description']
    list_filter = ('scheduled_status', 'start_date', 'end_date', 'created_on')
    summernote_fields = ('description',)


@admin.register(ExhibitionRegistration)
class ExhibitionRegistrationAdmin(admin.ModelAdmin):
    """
    Admin configuration for ExhibitionRegistration model,
    with key information on display list and filtering options

    """

    list_display = (
        'product_description', 'is_read', 'business_name',
        'registration_date', 'phone_number',
        )
    list_filter = ('registration_date', 'business_name')
    search_fields = ('business_name',)
