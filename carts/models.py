from django.db import models
from store.models import Product, Variation

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # variations = models.ManyToManyField(Variation, blank=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product_name
    
    def sub_total(self):
        return self.product.price * self.quantity

