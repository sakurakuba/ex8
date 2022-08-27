from django import forms
from review.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["author", "text", "score"]
