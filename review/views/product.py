from django.shortcuts import render
from django.views.generic import ListView
from review.models import Product


# Create your views here.
class IndexView(ListView):
    model = Product
    template_name = "product/index.html"
    context_object_name = "products"

