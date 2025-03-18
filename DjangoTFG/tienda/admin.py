from django.contrib import admin
from .models import Tienda, Categoria, Producto

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "description")
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "description", "categoria")
    
# Register your models here.
admin.site.register(Tienda, TaskAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
