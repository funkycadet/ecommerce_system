from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Product, Discount


class SerializerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Setting up test data
        self.parent_category = Category.objects.create(title="Electronics", description="All electronic items")
        self.sub_category = Category.objects.create(
            title="Mobiles", description="Smartphones and accessories", parent=self.parent_category
        )
        self.product = Product.objects.create(
            title="iPhone 14",
            description="Latest iPhone model",
            price=1000.00,
            stock_quantity=50,
            category=self.sub_category,
        )
        self.discount = Discount.objects.create(
            product=self.product, discount_type="percentage", amount=10
        )

    def test_category_serializer_serialization(self):
        """Test CategorySerializer serialization"""
        serializer_data = CategorySerializer(instance=self.parent_category).data
        self.assertEqual(serializer_data["name"], "Electronics")
        self.assertEqual(serializer_data["description"], "All electronic items")
        self.assertEqual(len(serializer_data["subcategories"]), 1)
        self.assertEqual(serializer_data["subcategories"][0]["name"], "Mobiles")

    def test_category_serializer_deserialization(self):
        """Test CategorySerializer deserialization"""
        data = {
            "name": "Home Appliances",
            "description": "Appliances for home use",
            "parent": self.parent_category.id,
        }
        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid())
        category = serializer.save()
        self.assertEqual(category.title, "Home Appliances")
        self.assertEqual(category.parent, self.parent_category)

    def test_product_serializer_serialization(self):
        """Test ProductSerializer serialization"""
        serializer_data = ProductSerializer(instance=self.product).data
        self.assertEqual(serializer_data["name"], "iPhone 14")
        self.assertEqual(serializer_data["price"], "1000.00")
        self.assertEqual(serializer_data["stock_quantity"], 50)
        self.assertEqual(serializer_data["category"], self.sub_category.id)

    def test_product_serializer_deserialization(self):
        """Test ProductSerializer deserialization"""
        data = {
            "name": "Samsung Galaxy S23",
            "description": "Newest Galaxy phone",
            "price": 900.00,
            "stock_quantity": 40,
            "category": self.sub_category.id,
        }
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        self.assertEqual(product.title, "Samsung Galaxy S23")
        self.assertEqual(product.category, self.sub_category)

    def test_discount_serializer_serialization(self):
        """Test DiscountSerializer serialization"""
        serializer_data = DiscountSerializer(instance=self.discount).data
        self.assertEqual(serializer_data["product"], self.product.id)
        self.assertEqual(serializer_data["discount_type"], "percentage")
        self.assertEqual(serializer_data["amount"], "10.00")

    def test_discount_serializer_deserialization(self):
        """Test DiscountSerializer deserialization"""
        data = {
            "product": self.product.id,
            "discount_type": "fixed",
            "amount": 50.00,
        }
        serializer = DiscountSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        discount = serializer.save()
        self.assertEqual(discount.product, self.product)
        self.assertEqual(discount.amount, 50.00)

