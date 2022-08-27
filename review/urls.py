from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from review.views import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView
from review.views.review import CreateReview, UpdateReview, DeleteReview

app_name = "review"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/review/add/', CreateReview.as_view(), name="review_create"),
    path('reviews/<int:pk>/update/', UpdateReview.as_view(), name="review_update"),
    path('reviews/<int:pk>/delete/', DeleteReview.as_view(), name="review_delete"),
]

