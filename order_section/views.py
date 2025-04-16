from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from .models import Card,Order,Order_items,Order_address
from product.models import Product_varient
from accounts.models import User_data,Vendor
from django.contrib.auth.decorators import login_required
from accounts.views import calculate_price
from django.http import HttpResponse


@login_required
def add_to_cart(request):
    #customar_id = User_data.objects.get(id=1)
    if request.method == "POST":
        print("add to card")
        user = request.user
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product_varient, id=product_id)
        session_id = request.session.session_key
        #print(product.title_pv)
        if not session_id:
            request.session.create()
            session_id = request.session.session_key

        cart_item, created = Card.objects.get_or_create(
            customar_id=user,
            product_varient_id=product,
            defaults={"quantity": 1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Redirect back to the same page
        return redirect(request.META.get('HTTP_REFERER', '/'))

    return JsonResponse({"error": "Invalid request"}, status=400)
        


# Create your views here.
@login_required
def shopping_card(request):
    total_price = calculate_price(request)
    user = request.user
    cart_items = Card.objects.filter(customar_id=user)
    card_number  = len(cart_items)
    return render(request, 'shoping-cart.html',{"cart_items":cart_items,"card_number":card_number,"total_price":total_price})

def Checkout(request):
    cart_value = Card.objects.filter(customar_id=request.user)
    price_t=0
    for i in cart_value:
        price_t= price_t+i.product_varient_id.price*i.quantity
    card_number  = len(cart_value)
    return render(request, 'checkout.html',{"card_number":card_number,"cart_value":cart_value,"price_t":price_t})

def remove_from_cart(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        try:
            cart_item = Card.objects.get(id=item_id, customar_id=request.user)
            cart_item.delete()
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)
        



@login_required
def update_cart(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))
        
        try:
            cart_item = Card.objects.get(id=item_id)
            cart_item.quantity = quantity
            cart_item.save()
            
            # Calculate new total for this item
            item_total = cart_item.product_varient_id.price * quantity
            return redirect(request.META.get('HTTP_REFERER', '/'))
            
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)


def Order_place(request):
    cart_value = Card.objects.filter(customar_id=request.user)
    price_t=0
    vendor_id =Vendor.objects.get(id=1)
    for i in cart_value:
        price_t= price_t+i.product_varient_id.price*i.quantity
        i.product_varient_id.Total_stock=i.product_varient_id.Total_stock-i.quantity
        i.product_varient_id.save()
    pay_taka=0
    for i in cart_value:
        pay_taka= pay_taka+i.product_varient_id.price*i.quantity
    print(pay_taka)
    
    order_place = Order.objects.create(
        customar_id=request.user,
        total_price=price_t,
        status="active"
    )
    for card_val in cart_value:
        order_item = Order_items.objects.create(
            customar_id=request.user,
            order_id = order_place,
            vendor_id=vendor_id,
            product_varient_id=card_val.product_varient_id,
            price=12,
            cupon="R45RT45RRR",
        )
    
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        division = request.POST.get("division")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip_code")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        type_address = request.POST.get("type_address")
        number = request.POST.get("number")
        
        order_add = Order_address.objects.create(
            customar_id=request.user,
            order_id=order_place,
            division=division,
            city=city,
            zip_code=zip_code,
            address_line1=address1,
            address_line2=address2,
            type_address=type_address
        )
        cart_value.delete()
    
    return redirect("initiate_payment",price=int(pay_taka))