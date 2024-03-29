from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    # product_variation = []
    # if request.method == "POST":
    #     for item in request.POST:
    #         key = item
    #         value = request.POST[key]
    #         try:
    #             variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
    #             # print(variation)
    #             product_variation.append(variation)
    #         except:
    #             pass    
    try:
        cart =  Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))
    cart.save()

    size = request.POST.get('size')
    color = request.POST.get('color')

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, size=size, color=color)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(product=product, cart=cart, quantity=1, size=size, color=color)

    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart, is_active = True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity        
    except Cart.DoesNotExist as e:
        print(f'error: {str(e)}')

    context = {
        "total" : total,
        "quantity" : quantity,
        "cart_items" : cart_items
    }
    return render(request, 'store/cart.html', context)

def remove_cart_item(request, item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    card_item_id = get_object_or_404(CartItem, id = item_id)
    cart_items = CartItem.objects.get(id = card_item_id.id, cart = cart)
    if cart_items:
        cart_items.delete()
    return redirect('cart')

def increase_item_quantity(request, item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    
    if cart_item.quantity > 0:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def decrease_item_quantity(request, item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    if (cart_item.quantity>1):
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')