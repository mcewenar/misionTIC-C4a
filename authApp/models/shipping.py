from django.db import models

class Shipping(models.Model):
    Shipping_id = models.AutoField(primary_key=True)
    conveyor = models.CharField(max_length=64, choices=(
        ('S', 'Servientrega'),
        ('T', 'TCC'),
        ('F', 'Fedex'),
        ('D', 'DHL'),
    ))
    delivery_time = models.DateTimeField()
    was_delivered = models.BooleanField()