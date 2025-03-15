from django import forms
from .models import ExhibitionRegistration


class ExhibitionRegistrationForm(forms.ModelForm):
    """
    Registering exhibitors for an exhibition.

    """
    class Meta:
        model = ExhibitionRegistration
        fields = (
            "registration_date",
            "business_name",
            "address",
            "email",
            "phone_number",
            "product_description",
            )
