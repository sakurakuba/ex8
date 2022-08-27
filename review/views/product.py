from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from review.forms import ProductForm
from review.models import Product


# Create your views here.
class IndexView(ListView):
    model = Product
    template_name = "product/index.html"
    context_object_name = "products"


class ProductView(DetailView):
    model = Product
    template_name = 'product/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.products.order_by("-created_at")
        u = self.request.user.groups.filter(name__in=['Moderators']).exists()
        context['u'] = u
        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'
    permission_required = "review.add_product"

    def get_success_url(self):
        return reverse('review:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    permission_required = "review.change_product"

    def get_success_url(self):
        return reverse('review:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('review:index')
    permission_required = "review.delete_product"
