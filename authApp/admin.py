from django.contrib import admin
from .models.customer import Customer
from .models.shipping import Shipping
from .models.order import Order
from .models.provider import Provider
from .models.category import Category

class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'name', 'email', 'address', 'phone', 'city')
    search_fields = ['name']
    list_filter = ('id',)

admin.site.register(Customer, CustomerAdmin)

class ShippingAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('Shipping_id', 'conveyor', 'delivery_time', 'was_delivered')
    search_fields = ['was_delivered']
    list_filter = ('Shipping_id',)

admin.site.register(Shipping, ShippingAdmin)

class OrdergAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('Order_id', 'customer_id', 'shipping_id', 'payment_method', 'shipping_address', 'date')
    search_fields = ['Order_id']
    list_filter = ('Order_id',)

admin.site.register(Order, OrdergAdmin)

class ProviderAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('provider_id', 'company', 'contact_name', 'address', 'city','phone', 'email')
    search_fields = ['company']
    list_filter = ('city',)

admin.site.register(Provider, ProviderAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('category_id', 'categories', 'description')
    search_fields = ['categories']
    list_filter = ('categories',)

admin.site.register(Category, CategoryAdmin)