from django.shortcuts import render
from .models import Exhibition

# Create your views here.


def up_coming_exhibition(request):
    exhibition = Exhibition.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "exhibition/exhibition.html",
        {"exhibition": exhibition},
    )
