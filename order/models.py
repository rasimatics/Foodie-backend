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


STATUS_CHOICES = (
    ('Not Taken', 'Not Taken'),
    ('Taken', 'Taken'),
    ('Delivered', 'Delivered'),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, null=True, blank=True)
    delivery_method = models.CharField(max_length=30, choices=DELIVERY_CHOICES, null=True, blank=True)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, null=True, blank=True)
    accepted = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_amount(self):
        return sum(item.get_price() for item in self.items.all())

    def __str__(self):
        return f"Order-{self.id} at {self.created_at}"


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()

    def get_price(self):
        return self.item.price * self.quantity

    def __str__(self):
        return f"Order - {self.item}"
