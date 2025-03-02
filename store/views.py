from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.http import HttpResponse
from .models import Product


# Create your views here.


# def my_store(request):
# return HttpResponse('Hello, Store')

class product_list(generic.ListView):
    """View to list of published products with pagination."""

    template_name = "store/index.html"
    paginate_by = 12
    queryset = None

    def get_queryset(self):
        """Return a queryset of published products."""
        if self.queryset is None:
            self.queryset = Product.objects.filter(status=1)
        return self.queryset


def product_detail(request, slug):
    queryset = Product.objects.filter(status=1)
    product = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        'store/product_detail.html',
        {"product": product},
    )


# from django.shortcuts import render
# from .models import Product
# def product_list(request):
    # products = Product.objects.all()
    # return render(request, 'myapp/index.html', {'products': products})
# def product_detail(request, pk):
    # product = Product.objects.get(pk=pk)
    # return render(request, 'myapp/index2.html', {'product': product})
# from django.http import HttpResponse
# def home(request):
    # return HttpResponse('Hello, World!')
