from inventory.models import *
from rest_framework import viewsets,permissions,mixins
from .serializer import  AllProducts, CategorySerializer, ProductInventorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, query=None):
        queryset = Product.objects.filter(category__slug=query)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class AllProductsViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"                      


    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)[:10]
        serializer = AllProducts(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin
    ):
    queryset = ProductInventory.objects.all()
    
    def list(self,request, slug=None):
        queryset = ProductInventory.objects.filter(
            product__category__slug=slug
        ).filter(is_default=True)[:10]
        serializer = ProductInventorySerializer(queryset, context={'request':request} ,many=True)

        return Response(serializer.data)


    