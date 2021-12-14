from django.db import models
from .type import Type

class Products(models.Model):
    id_products = models.IntegerField(primary_key=True)
    name_product = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank = True)
    stock = models.PositiveIntegerField('Stock')
    type_product = models.ForeignKey( Type, on_delete=models.CASCADE)