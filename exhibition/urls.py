from django.urls import path
from . import views

urlpatterns = [
    path("", views.up_coming_exhibition, name='exhibition'),
]
