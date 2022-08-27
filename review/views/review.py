from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from review.forms import ReviewForm
from review.models import Product, Review


class CreateReview(LoginRequiredMixin, CreateView):
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


class UpdateReview(PermissionRequiredMixin, UpdateView):
    form_class = ReviewForm
    template_name = "review/review_update.html"
    model = Review
    permission_required = "review.change_review"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse("review:product_view", kwargs={"pk": self.object.product.pk})


class DeleteReview(PermissionRequiredMixin, DeleteView):
    model = Review
    permission_required = "review.delete_review"

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse("review:product_view", kwargs={"pk": self.object.product.pk})
