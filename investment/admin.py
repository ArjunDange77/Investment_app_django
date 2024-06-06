from django.contrib import admin
from .models import Customer, ProductMaster, Investment

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name')
    search_fields = ('customer_name',)

class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')
    search_fields = ('product_name',)

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'investment_amount')
    list_filter = ('customer', 'product')
    search_fields = ('customer__customer_name', 'product__product_name')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(ProductMaster, ProductMasterAdmin)
admin.site.register(Investment, InvestmentAdmin)
