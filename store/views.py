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
    reviews = product.review_set.all().order_by('-created_at')
    review_count = product.review_set.filter(is_approved=True).count()

    context = {
        "product": product,
        "reviews": reviews,
        "review_count": review_count
    }

    return render(
        request,
        'store/product_detail.html',
        context
    )
