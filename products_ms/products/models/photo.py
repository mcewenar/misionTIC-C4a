from django.db import models
from .products import Products

class Photo(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey( Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', null=True, max_length=255) 
    