from .models import ExhibitionRegistration
from django import forms


class ExhibitionRegistrationForm(forms.ModelForm):
    class Meta:
        model = ExhibitionRegistration
        fields = (
            "business_name",
            "address",
            "email",
            "phone_number",
            "product_description"
            )
