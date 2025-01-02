import django_filters
from .models import Product
from rest_framework import filters 


class ProductFilter(django_filters.FilterSet):
    class Meta:
        created_at = django_filters.DateFilter(field_name='created_at__date')
        model = Product
        fields = {
            'title': ['icontains'],
            'price': ['lt', 'gt'],
            'stock_quantity': ['lt', 'gt'],
            'category': ['exact'],
        }


