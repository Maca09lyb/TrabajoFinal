"""TPintegrador URL Configuration

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
from shop.views import agregar_producto, registro, modificar_producto, eliminar_producto, acercade
from django.contrib import admin
from django.urls import path,include
from shop import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro, name='registro'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('filtro_secciones/<int:seccion_id>', views.filtro_secciones, name="filtro_secciones"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('acercade/', acercade, name="acercade"),  
]
