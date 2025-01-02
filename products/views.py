from json import JSONDecodeError
from django.http import JsonResponse
from .serializer import CategorySerializer, ProductSerializer, DiscountSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .models import Category, Product, Discount
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny


class CategoryView(views.APIView):
    # permission_classes = [AllowAny]

    serializer_class = CategorySerializer

    # def get_serializer_context(self):
    #     return {
    #         'request': self.request
    #         'format': self.format_kwarg,
    #         'view': self
    #     }

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Category.objects.all()

    # def get_extra_actions(self):
    #     return []

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(views.APIView):
    # permission_classes = [AllowAny]

    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def get_many_products(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_one(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def get_queryset(self):
        return Product.objects.all()

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiscountView(views.APIView):
    # permission_classes = [AllowAny]

    serializer_class = DiscountSerializer

    # def get(self, request):
    #     discounts = Discount.objects.all()
    #     serializer = DiscountSerializer(discounts, many=True)
    #     return Response(serializer.data)

    # def get_queryset(self):
    #     return Discount.objects.all()

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = DiscountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

