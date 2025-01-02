from django.contrib import admin
from .models import Category, Product, Discount


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    search_fields = ['title']
    list_filter = ['parent']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock_quantity', 'category']
    search_fields = ['title']
    list_filter = ['category']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_type', 'amount']
    search_fields = ['product']
    list_filter = ['discount_type']

