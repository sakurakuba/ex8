from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from review.forms import ReviewForm
from review.models import Product, Review


class CreateReview(CreateView):
    form_class = ReviewForm
    template_name = "review/review_create.html"

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        user = self.request.user
        form.instance.product = product
        form.instance.author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("review:product_view", kwargs={"pk": self.object.product.pk})


class UpdateReview(UpdateView):
    form_class = ReviewForm
    template_name = "review/review_update.html"
    model = Review

    def get_success_url(self):
        return reverse("review:product_view", kwargs={"pk": self.object.product.pk})


class DeleteReview(DeleteView):
    model = Review

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("review:product_view", kwargs={"pk": self.object.product.pk})
