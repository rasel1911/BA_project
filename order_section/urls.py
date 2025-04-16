from .views import shopping_card,Checkout,add_to_cart,update_cart,remove_from_cart,Order_place
from django.urls import path


urlpatterns = [
    path('shoppingcard/',shopping_card, name="shoppingcard"),
    path('checkout/',Checkout, name="checkout"),
    path("cart/add/", add_to_cart, name="add_to_cart"),
    path('update-cart/', update_cart, name='update_cart'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('order_place/', Order_place, name='order_place'),
    
]