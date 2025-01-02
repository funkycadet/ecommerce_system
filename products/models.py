from django.db import models
from utils.models_abstract import Model
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
)


class Category(Model, ActivatorModel, TimeStampedModel, TitleDescriptionModel):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ["id"]

    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories'
    )

    def __str__(self) -> str:
        return f'{self.title}'


class Product(Model, ActivatorModel, TimeStampedModel, TitleDescriptionModel):

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["id"]

    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self) -> str:
        return f'{self.title}'

    @property
    def final_price(self):
        # Calculate final price considering the highest discount
        discounts = self.discounts.all()
        if not discounts:
            return self.price
        max_discount = max(
            [discount.calculate_discounted_price(self.price) for discount in discounts]
        )
        return max_discount


class Discount(Model, TimeStampedModel, TitleDescriptionModel):

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'
        ordering = ["id"]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discounts')
    discount_type = models.CharField(
        max_length=10, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed')]
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_discounted_price(self, price):
        if self.discount_type == 'percentage':
            return price - (price * (self.amount / 100))
        elif self.discount_type == 'fixed':
            return price - self.amount
        return price

    def __str__(self):
        return self.amount
        # return f"{self.get_discount_type_display()} - {self.amount}"

