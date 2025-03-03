from django.contrib import admin
from .models import Exhibition
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
