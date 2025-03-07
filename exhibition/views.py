from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Exhibition
from .forms import ExhibitionRegistrationForm

# Create your views here.


def up_coming_exhibition(request):
    exhibition = Exhibition.objects.all().order_by('-updated_on').first()

    if request.method == 'POST':
        exhibition_registration_form = ExhibitionRegistrationForm(
            data=request.POST
            )
        if exhibition_registration_form.is_valid():
            exhibition_registration_form.save()
            messages.success(
                request, "Your registration for the exhibition has been successfully submitted!") # noqa
            return redirect('exhibition')
    else:
        exhibition_registration_form = ExhibitionRegistrationForm()

    return render(
        request,
        "exhibition/exhibition.html",
        {
            "exhibition": exhibition,
            "exhibition_registration_form": exhibition_registration_form
        },
    )
