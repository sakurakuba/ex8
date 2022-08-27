from django.urls import path

from review.views import IndexView

app_name = "review"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
