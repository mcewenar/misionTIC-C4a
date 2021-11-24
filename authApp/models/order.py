from django.db import models
from .customer import Customer
from .shipping import Shipping

class Order(models.Model):
    Order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, related_name="Customer_Order", on_delete=models.SET_NULL, null=True)
    shipping_id = models.ForeignKey(Shipping, related_name="Shipping_Order", on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=64, choices=(
        ('C', 'Credito'),
        ('D', 'Debito'),
        ('P', 'paypal'),
        ('N', 'Nequi'),
    ))
    shipping_address = models.CharField(max_length=60)
    date = models.DateTimeField()