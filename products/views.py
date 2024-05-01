from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    SAFE_METHODS,
    BasePermission,
)
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class ProductsAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, productId):
        product=get_object_or_404(Product, pk=productId)
        self.check_object_permissions(self.request, product)
        return product

    def get(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, productId):
        product = self.get_object(productId)
        product.delete()
        data = {"product": f"{product} is deleted."}
        return Response(data, status=status.HTTP_200_OK)
