from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Creating or updating Review instances with a form.

    Associated with Review model, includes a single field
    and also provides custom validation for the body field.
    """
    class Meta:
        model = Review
        fields = ("body",)

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body:
            raise forms.ValidationError("This field cannot be empty.")
        return body
