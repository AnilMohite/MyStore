from django.contrib import admin
from .models import Product, Variation

class ProductAdmin(admin.ModelAdmin):    
    list_display = ('product_name','price','stock','category','is_available','modified_date')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)