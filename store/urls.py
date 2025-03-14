from . import views
from django.urls import path


urlpatterns = [
    path("", views.product_list.as_view(), name="home"),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path("<slug:slug>/edit_review/<int:review_id>",
         views.update_review, name="update_review"),
    path("<slug:slug>/delete_review/<int:review_id>",
         views.delete_review, name="delete_review"),
]
