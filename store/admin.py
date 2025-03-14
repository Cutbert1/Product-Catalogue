from django.contrib import admin
from .models import Product, Review
from django_summernote.admin import SummernoteModelAdmin
from django.core.exceptions import FieldDoesNotExist # noqa
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Admin class for managing Product model in the Django admin interface.
    This class extends SummernoteModelAdmin to provide
    rich text editing capabilities.
    """

    list_display = ('name', 'price', 'status', 'created_on', 'updated_on')
    search_fields = ['name', 'description']
    list_filter = ('status', 'updated_on')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.validate_fields()

    def validate_fields(self):
        model_fields = [field.name for field in self.model._meta.get_fields()]

        self.validate_list_display(model_fields)
        self.validate_search_fields(model_fields)
        self.validate_list_filter(model_fields)
        self.validate_prepopulated_fields(model_fields)
        self.validate_summernote_fields(model_fields)

    def validate_list_display(self, model_fields):
        for field in self.list_display:
            if field not in model_fields:
                raise admin.ValidationError(
                    _(
                        "Field '%(field)s' in list_display does not exist in model %(model)s."), # noqa
                    params={'field': field, 'model': self.model.__name__},
                )

    def validate_search_fields(self, model_fields):
        for field in self.search_fields:
            if field not in model_fields:
                raise admin.ValidationError(
                    _("Field '%(field)s' in search_fields does not exist in model %(model)s."), # noqa
                    params={'field': field, 'model': self.model.__name__},
                )

    def validate_list_filter(self, model_fields):
        for field in self.list_filter:
            if field not in model_fields:
                raise admin.ValidationError(
                    _("Field '%(field)s' in list_filter does not exist in model %(model)s."), # noqa
                    params={'field': field, 'model': self.model.__name__},
                )

    def validate_prepopulated_fields(self, model_fields):
        for field, sources in self.prepopulated_fields.items():
            if field not in model_fields:
                raise admin.ValidationError(
                    _("Field '%(field)s' in prepopulated_fields does not exist in model %(model)s."), # noqa
                    params={'field': field, 'model': self.model.__name__},
                )

            for source in sources:
                if source not in model_fields:
                    raise admin.ValidationError(
                        _("Source field '%(field)s' for '%(target)s' in prepopulated_fields does not exist in model %(model)s."), # noqa
                        params={'field': source, 'target': field, 'model': self.model.__name__}, # noqa
                    )

    def validate_summernote_fields(self, model_fields):
        for field in self.summernote_fields:
            if field not in model_fields:
                raise admin.ValidationError(
                    _("Field '%(field)s' in summernote_fields does not exist in model %(model)s."), # noqa
                    params={'field': field, 'model': self.model.__name__},
                )


admin.site.register(Review)
