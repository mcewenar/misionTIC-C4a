from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    categories = models.CharField(max_length=64, choices=(
        ('S', 'Ciclismo'),
        ('T', 'Atletismo'),
        ('F', 'Boxeo'),
        ('D', 'Futbol'),
        ('S', 'Voleibol'),
        ('T', 'Baloncesto'),
        ('F', 'Natacion'),
        ('D', 'Tenis'),
    ))
    description  = models.TextField(null=True, blank=True)