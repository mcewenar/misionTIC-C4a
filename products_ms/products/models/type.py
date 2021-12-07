from django.db import models

class Type(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField('Type Name', max_length=150)