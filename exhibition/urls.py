from . import views
from django.urls import path


urlpatterns = [
    path("", views.up_coming_exhibition, name='exhibition'),
]
