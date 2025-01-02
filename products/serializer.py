from django.db import models
from rest_framework import serializers
from rest_framework.fields import CharField
from . import models


class CategorySerializer(serializers.ModelSerializer):

    name = CharField(source="title", required=True)
    # description = CharField(source="description", required=False)
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['name', 'description', 'parent', 'subcategories', 'created_at', 'updated_at']

    def get_subcategories(self, obj):
        return CategorySerializer(obj.subcategories.all(), many=True).data

class ProductSerializer(serializers.ModelSerializer):

    name = CharField(source="title", required=True)
    final_price = serializers.ReadOnlyField()

    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'final_price', 'stock_quantity', 'category', 'created_at', 'updated_at']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Discount
        fields = ['product', 'discount_type', 'amount', 'created_at']
