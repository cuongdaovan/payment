from django.contrib import admin
# Register your models here.
from myFirstApp import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","description"]
    search_fields = ["name"]
    list_filter = ["name"]
    
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.Order_item)
