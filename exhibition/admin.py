from django.contrib import admin
from .models import Exhibition, ExhibitionRegistration
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Exhibition)
class ExhibitionAdmin(SummernoteModelAdmin):

    list_display = (
        'title', 'start_date', 'end_date', 'scheduled_status', 'created_on',
        'max_attendees')
    search_fields = ['title', 'description']
    list_filter = ('scheduled_status', 'start_date', 'end_date', 'created_on')
    summernote_fields = ('description',)


@admin.register(ExhibitionRegistration)
class ExhibitionRegistrationAdmin(admin.ModelAdmin):

    list_display = (
        'product_description', 'is_read', 'business_name', 'registration_date',
        )
    list_filter = ('registration_date', 'business_name')
    search_fields = ('business_name',)
