from django.db import models
class Customer(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField('Name', max_length = 30)
        user = models.CharField('User', max_length = 30)
        email = models.EmailField('Email', max_length = 100)
        address = models.CharField('Address', max_length = 100)
        phone = models.CharField('Phone', max_length = 100)
        city = models.CharField('City', max_length = 30)
