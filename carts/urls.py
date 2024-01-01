from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("add_cart/<int:product_id>", views.add_cart, name="add_cart"),
    path("remove_cart_item/<int:product_id>", views.remove_cart_item, name="remove_cart_item"),
    path("increase_item_quantity/<int:product_id>", views.increase_item_quantity, name="increase_item_quantity"),
    path("decrease_item_quantity/<int:product_id>", views.decrease_item_quantity, name="decrease_item_quantity"),
]
