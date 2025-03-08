from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Product, Review
from .forms import ReviewForm


# Create your views here.


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
            return ReviewForm()
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


def review_edit(request, review_id, product_slug):
    if request.method == "POST":
        product = get_product_by_slug(product_slug)
        review = get_review_by_id(review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if is_review_editable(review_form, review, request.user):
            save_review(review_form, product)
            messages.success(request, "Review Updated")
        else:
            messages.error(request, "Error updating review")

    return redirect_to_product_detail(product_slug)


def get_product_by_slug(slug):
    queryset = Product.objects.filter(status=1)
    return get_object_or_404(queryset, slug=slug)


def get_review_by_id(review_id):
    return get_object_or_404(Review, pk=review_id)


def is_review_editable(review_form, review, user):
    return review_form.is_valid() and review.author == user


def save_review(review_form, product):
    review = review_form.save(commit=False)
    review.product = product
    review.is_approved = False
    review.save()


def redirect_to_product_detail(slug):
    return redirect("product_detail", slug=slug)
