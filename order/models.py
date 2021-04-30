from django.db import models
from user.models import User
from product.models import Item

DELIVERY_CHOICES = (
    ('Door delivery', 'Door delivery'),
    ('Pick up', 'Pick up')
)


PAYMENT_CHOICES = (
    ('Card', 'Card'),
    ('Bank Account', 'Bank Account'),
    ('Paypal', 'Paypal'),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    delivery_method = models.CharField(max_length=30, choices=DELIVERY_CHOICES, null=True, blank=True)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s order"


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order - {self.item}"
