from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Exhibition
from .forms import ExhibitionRegistrationForm

# Create your views here.


def up_coming_exhibition(request):
    """
    Upcoming exhibition page and registration process.

    GET the most recent exhibition from the database.
    Processes the exhibition registration form submission.
    Renders the exhibition page with the exhibition
    details and registration form.

    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponse: Rendered response of the exhibition page or a redirect
                      to the exhibition page when form submission is
                      successful.

    """
    exhibition = Exhibition.objects.all().order_by('-updated_on').first()

    if request.method == 'POST':
        exhibition_registration_form = ExhibitionRegistrationForm(
            data=request.POST
            )
        if exhibition_registration_form.is_valid():
            exhibition_registration_form.save()
            messages.success(
                request, "Your registration for the exhibition has been successfully submitted!")  # noqa
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
