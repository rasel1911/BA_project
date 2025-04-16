# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('initiate-payment/<int:price>/', views.initiate_payment, name='initiate_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/fail/', views.payment_fail, name='payment_fail'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
]
