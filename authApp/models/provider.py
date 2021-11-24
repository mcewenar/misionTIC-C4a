from django.db import models

class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    company = models.CharField('Company', max_length=30)
    contact_name= models.CharField('Contact name', max_length=50)
    address = models.CharField('Address', max_length=100)
    city = models.CharField('City', max_length=20,choices=(
        ('Barranquilla', 'Barranquilla'),
        ('Bogotá', 'Bogotá'),
        ('Cali', 'Cali'),
        ('Manizales', 'Manizales'),
        ('Medellín', 'Medellín')        
    ))
    phone = models.CharField('Phone', max_length=12)
    email = models.EmailField('Email', max_length = 256)
