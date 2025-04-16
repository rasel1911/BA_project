# views.py

import requests
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def payment_success(request):
    return JsonResponse({'message': 'Payment was successful'})

@csrf_exempt
def payment_fail(request):
    return JsonResponse({'message': 'Payment failed'})

@csrf_exempt
def payment_cancel(request):
    return JsonResponse({'message': 'Payment cancelled'})



@csrf_exempt
def initiate_payment(request,price):
    post_data = {
        'store_id': settings.SSLCOMMERZ_STORE_ID,
        'store_passwd': settings.SSLCOMMERZ_STORE_PASS,
        'total_amount': price,  # dynamically set this
        'currency': 'BDT',
        'tran_id': 'unique_transaction_id_12345',
        'success_url': request.build_absolute_uri('/payment/success/'),
        'fail_url': request.build_absolute_uri('/payment/fail/'),
        'cancel_url': request.build_absolute_uri('/payment/cancel/'),
        'emi_option': 0,
        'cus_name': 'Customer Name',
        'cus_email': 'customer@example.com',
        'cus_phone': '01700000000',
        'cus_add1': 'Customer Address',
        'cus_city': 'Dhaka',
        'cus_country': 'Bangladesh',
        'shipping_method': 'NO',
        'product_name': 'Demo Product',
        'product_category': 'Demo',
        'product_profile': 'general',
    }

    response = requests.post(settings.SSLCOMMERZ_INIT_URL, data=post_data)
    data = response.json()

    if data.get('status') == 'SUCCESS':
        return redirect(data['GatewayPageURL'])
    else:
        return JsonResponse({'error': 'Payment initiation failed'})
