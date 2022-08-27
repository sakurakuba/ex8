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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'

    def get_success_url(self):
        return reverse('review:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse('review:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('review:index')
