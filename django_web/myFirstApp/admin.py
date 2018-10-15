from django.contrib import admin

# Register your models here.
from .models import Product,Category,Customer,Order,Order_item

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","description"]
    search_fields = ["name"]
    list_filter = ["name"]
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Order_item)

