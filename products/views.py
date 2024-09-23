from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from rest_framework_api_key.permissions import HasAPIKey


class ProductListView(ListAPIView):
    serializer_class= ProductSerializer
    queryset= Product.objects.all()
    permission_classes= [HasAPIKey]