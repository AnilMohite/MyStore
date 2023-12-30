from django.shortcuts import render
from .models import Product

def store(request):
    products = Product.objects.filter(is_available=True)
    total_products = products.count()
    context = {
        'products':products,
        'total_products':total_products
    }
    return render(request, 'store/store.html', context)
