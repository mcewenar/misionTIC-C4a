from proveedoresApp.views.proveedorView import ProveedorListCreateView, ProveedorRetrieveUpdateDestroy
#from proveedoresApp.views.proveedorView import proveedorApi
from django.contrib import admin
from django.urls import path
from proveedoresApp import views
#from django.conf.urls import url,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('proveedores/',views.ProveedorListCreateView.as_view()), #Ver todos los proveedores, crear un proveedor. Usar / al final
    path('proveedor/<int:pk>/',views.ProveedorRetrieveUpdateDestroy.as_view()), #Borrar, editar y consultar un proveedor. Con / al final
]


#urlpatterns = [ 
#    path('admin/', admin.site.urls), 
#    url(r'^',include('proveedoresApp.urls'))
#]
 
#urlpatterns = [ 
#    url(r'^admin/$', views.tutorial_list), #GET, POST, DELETE. GET list of tutorials, POST a new tutorial, DELETE all tutorials
#    url(r'^proveedor/(?P<pk>[0-9]+)$', views.tutorial_detail), #GET, PUT, DELETE. GET / PUT / DELETE tutorial by ‘id’
#    url(r'^proveedores/$', views.tutorial_list_published), #GET. GET all published tutorials
#    url(r'^', include('proveedoresApp.urls'))
#]




"""proveedoresProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""