from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
    STATUS_CHOICES = [
        ('Complete', 'Complete'),
        ('Deliver in one week', 'Deliver in one week'),
        ('Deliver in three days', 'Deliver in three days'),
        ('Arrive today', 'Arrive today'),
        ('Order Confirmed', 'Order Confirmed'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Order Confirmed')

    def __str__(self):
        return f"Order {self.id} by {self.customer}"