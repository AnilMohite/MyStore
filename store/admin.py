from django.contrib import admin
from .models import Product, Variation

class ProductAdmin(admin.ModelAdmin):    
    list_display = ('product_name','price','stock','category','is_available','modified_date')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product, ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_filter = ('variation_category',)
admin.site.register(Variation, VariationAdmin)