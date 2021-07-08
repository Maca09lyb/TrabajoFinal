from django.contrib import admin
from.models import Products
from.models import Order, Seccion
# Register your models here.

admin.site.site_header = "Jaguarete KAA S.A."
admin.site.site_tittle = "Tienda"
admin.site.index_title = "Gestión de la tienda"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','category','image')
    search_fields =('title',)


admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Seccion)