from django.contrib import admin
from .models import Glass,Order,OrderItem,Distributor,Category

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display= ["email","address","phone","distributor_type"]

@admin.register(Glass)
class GlassAdmin(admin.ModelAdmin):
    list_display= ['name','category','slug','is_active','in_stock','price','description','size']
    list_filter = ['in_stock','is_active','size','color','price']
    list_editable= ['price','in_stock']
    prepopulated_fields= {'slug':  ('name',)}