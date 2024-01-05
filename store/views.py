from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator

def store(request, category_slug=None):
    if category_slug != None:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category = category)
    else:
        products = Product.objects.filter(is_available = True)

    paginator = Paginator(products,6)
    page = request.GET.get('page')
    page_products = paginator.get_page(page)
    total_products = products.count()
    context = {
        'products':page_products,
        'total_products':total_products
    }
    return render(request, 'store/store.html', context)

def product_detail(request,category_slug=None,product_slug=None):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
    except Exception as e:
        raise e
    context = {
        'product' : single_product,
        'in_cart' : in_cart
    }
    return render(request, 'store/product-detail.html', context)

def search(request):
    if 'search' in request.path:
        q = request.GET.get('q')
        products = Product.objects.filter(product_name__icontains = q)
        # paginator = Paginator(products, 1)
        # page = request.GET.get('page')
        # page_products = paginator.get_page(page)
        total_products = products.count()
        context = {
            'products':products,
            'total_products':total_products
        }
        return render(request, 'store/store.html', context)
    return redirect('store')