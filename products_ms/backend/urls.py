
from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', views.ProductListCreateView.as_view()),
    path('products/<int:pk>', views.ProductRetrieveUpdateDestroy.as_view()),
    path('types', views.TypeListCreateView.as_view()),
    path('types/<int:pk>', views.TypeRetrieveUpdateDestroy.as_view()),
    path('photos', views.PhotoListCreateView.as_view()),
    path('photos/<int:pk>', views.PhotoRetrieveUpdateDestroy.as_view())
]
