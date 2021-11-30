from django.db import models
from django.core.validators import RegexValidator
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
class Proveedor(models.Model):
    idRegister = models.AutoField('idRegister',primary_key=True)
    name_company = models.CharField('Name_company',max_length=50,null=False, unique=True)
    name_contact = models.CharField('Name_contact',max_length=50,null=False)
    #validador de celular:
    phone_regex = phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    cel = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    address = models.CharField('Address',max_length=80,null=False)
    city = models.CharField('City',max_length=50,null=False)
    email = models.EmailField('Email', max_length = 100,null=True)
