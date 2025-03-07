from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("caption", "body")

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body:
            raise forms.ValidationError("This field cannot be empty.")
        return body
