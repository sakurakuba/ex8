from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from review.views import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = "review"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
