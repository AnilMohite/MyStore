from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug=None):
    if category_slug != None:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category = category)
    else:
        products = Product.objects.filter(is_available = True)
    total_products = products.count()
    context = {
        'products':products,
        'total_products':total_products
    }
    return render(request, 'store/store.html', context)

def product_detail(request,category_slug=None,product_slug=None):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    context = {
        'product':single_product
    }
    return render(request, 'store/product-detail.html', context)