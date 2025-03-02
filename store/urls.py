# from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path("", views.product_list.as_view(), name="home"),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
