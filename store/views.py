from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic
# from django.http import HttpResponse
from .models import Product
from .forms import ReviewForm


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


def get_product_and_reviews(slug):
    product = get_object_or_404(Product.objects.filter(status=1), slug=slug)
    reviews = product.review_set.all().order_by('-created_at')
    review_count = product.review_set.filter(is_approved=True).count()
    return product, reviews, review_count


def handle_review_submission(request, product):
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            messages.success(request, "Review submitted, awaiting approval")
    else:
        review_form = ReviewForm()
    return review_form


def product_detail(request, slug):
    product, reviews, review_count = get_product_and_reviews(slug)
    review_form = handle_review_submission(request, product)

    context = {
        "product": product,
        "reviews": reviews,
        "review_count": review_count,
        "review_form": review_form,
    }

    return render(
        request,
        'store/product_detail.html',
        context)
