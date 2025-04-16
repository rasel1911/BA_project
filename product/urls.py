from .views import shop_details,shop_grid,vendor_create,vendor_deshboard,vendor_product,vendor_product_varient,review_and_rating,vendor_product_order
from django.urls import path


urlpatterns = [
    path('shopdetails/<int:id>/', shop_details, name='shopdetailsId'),
    path('shopdetails/', shop_details, name='shopdetails'),
    path('shopgrid/',shop_grid, name="shopgrid"),
    path('vendorreg/',vendor_create, name="vendorreg"),
    path('vendorDeshboard/', vendor_deshboard, name='vendorDeshboard'),
    path('vendorProduct/', vendor_product, name='vendorProduct'),
    path('vendorVeriant/', vendor_product_varient, name='vendorVeriant'),
    path('reviewRating/<int:id>/', review_and_rating, name='reviewRating'),
    path('vendorOrder/', vendor_product_order, name='vendorOrder'),
]