from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductsAPIView.as_view()),
    path("<int:productId>", views.ProductDetailAPIView.as_view()),
]
