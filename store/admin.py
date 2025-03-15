from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Review

# Register your models here.


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    For managing Product model in admin interface.
    Extends SummernoteModelAdmin to deliver
    rich text editing functionalities.
    """

    list_display = ('name', 'price', 'status', 'created_on', 'updated_on')
    search_fields = ['name', 'description']
    list_filter = ('status', 'updated_on')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)


@admin.register(Review)
class Review(admin.ModelAdmin):
    """
    Defines the display, filtering, and search options
    for Review objects in admin interface.
    """

    list_display = (
        'product', 'author', 'is_approved',
        )
    list_filter = ('created_at',)
    search_fields = ('product',)
