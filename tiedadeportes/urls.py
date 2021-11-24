from django.contrib import admin
from django.urls import path
from authApp import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', views.CRUD_Order.as_view()),
    path('orders/<int:pk>', views.CRUD_Order2.as_view()),
    path('customers/', views.CustomerListCreateView.as_view()),
    path('customer/<int:pk>', views.CustomerRetrieveUpdateDestroy.as_view()),
    path('shippings/', views.ShippingListCreateView.as_view()),
    path('shipping/<int:pk>', views.ShippingRetrieveUpdateDestroy.as_view()),
    path('providers/', views.ProviderListCreateViews.as_view()),
    path('provider/<int:pk>', views.ProviderRetrieveUpdateDestroy.as_view())
]
