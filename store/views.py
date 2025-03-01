# from django.shortcuts import render
from django.views import generic
# from django.http import HttpResponse
from .models import Product


# Create your views here.


# def my_store(request):

   # return HttpResponse('Hello, Store')

class ProductListView(generic.ListView):
    """View to list of published products with pagination."""

    template_name = "store/index.html"
    paginate_by = 8
    queryset = None

    def get_queryset(self):
        """Return a queryset of published products."""
        if self.queryset is None:
            self.queryset = Product.objects.filter(status=1)
        return self.queryset
