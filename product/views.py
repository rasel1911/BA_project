
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Vendor,User_data
from .models import Unit,Color,Catagory,Size,Product,Product_image,Product_varient
from django.contrib.auth.decorators import login_required
from order_section.models import Card,Review_and_rating,Order_items
from accounts.views import calculate_price
from django.http import JsonResponse
from textblob import Word
from blog.views import extract_features , find_similar

# Create your views here.
def shop_details(request,id=0):
    total_price = calculate_price(request)
    commants = Review_and_rating.objects.filter(product_varient_id= id+3)
    if id is None:
        card_number  = len(Card.objects.all())
        return render(request, 'shop-details.html',{"card_number":card_number,"total_price":total_price,"commants":commants})
    else:
        card_number  = len(Card.objects.all())
        product_cat = Product_image.objects.get(id=id)
        pr=product_cat.product_varient_id.catagory_id.name
        product_v = Product_varient.objects.filter(catagory_id__name =pr )
            
        product_im =  get_object_or_404(Product_image, id=id)
        product_all = Product_image.objects.all()
        return render(request, 'shop-details.html',{"product_im":product_im,"card_number":card_number,"total_price":total_price,"commants":commants,"product_v":product_v,"product_all":product_all})
        

def shop_grid(request):
    card_number  = len(Card.objects.all())
    total_price = calculate_price(request)
    if request.method == "POST" and not 'image' in request.FILES:
        sea = request.POST.get("search")
        if sea:
            w = Word(sea)
            search=w.spellcheck()[0][0]
            print("post method success",search) 
            product_varient_iamge = Product_image.objects.filter(product_varient_id__title_pv__icontains=search)
            return render(request, 'shop-grid.html',{"product_varient_iamge":product_varient_iamge,"card_number":card_number,"total_price":total_price,"search":search})
    elif request.method == 'POST' and 'image' in request.FILES:
        uploaded_file = request.FILES["image"]
        features = extract_features(uploaded_file)
        similar_ids = find_similar(features)
        product_varient_iamge = Product_image.objects.filter(id__in=similar_ids)
        return render(request, 'shop-grid.html',{"product_varient_iamge":product_varient_iamge,"card_number":card_number,"total_price":total_price})
    else:
        product_varient_iamge = Product_image.objects.all()
        return render(request, 'shop-grid.html',{"product_varient_iamge":product_varient_iamge,"card_number":card_number,"total_price":total_price})


@login_required
def vendor_deshboard(request):
    #print("hemmo rasel")
    user_vendor = User_data.objects.get(id=5)
    vendors = Vendor.objects.get(id=1)
    final_product_v=Product_varient.objects.all()
    final_product_v_number = len(final_product_v)
    print(vendors.shop_name)
        
    return render(request, 'vendor_deshboard_last.html',{'vendors': vendors,"user_vendor":user_vendor,"final_product_v_number":final_product_v_number})

@login_required
def vendor_create(request):
    if request.method == "POST":
        user = request.user  # Get the currently logged-in user
        shop_name = request.POST.get('shop_name')
        address_vendor = request.POST.get('address_vendor')
        vendor_image = request.FILES.get('vendor_image')
        shop_slug = request.POST.get('shop_slug')
        description = request.POST.get('description')
        trad_license = request.POST.get('trad_license')

        if not shop_name or not address_vendor or not shop_slug or not description or not trad_license :
            return render(request, 'vendor_create.html', {'error': 'All required fields must be filled.'})

        # Create and save User_data object
        vendor_data= Vendor.objects.create(
            seller_id=user,
            shop_name=shop_name,
            address=address_vendor,
            image=vendor_image,
            rating=5,
            description=description,
            tradelicense=trad_license
        )
        return redirect('home')  # Redirect to home or another appropriate page

    return render(request, 'vendor_create.html')


@login_required
def vendor_product(request):
    print("hemmo rasel")
    user_vendor = User_data.objects.get(id=5)
    vendors = Vendor.objects.get(id=1)
    
    if request.method == "POST":
        #print("post mathod print")
        #user = request.user  # Get the currently logged-in user
        product_name = request.POST.get('product_name')
        product_des = request.POST.get('product_des')
        product_image = request.FILES.get('product_image')
        product_catagory = request.POST.get('product_catagory')
        product_price = request.POST.get('product_price')
        product_sku = request.POST.get('product_sku')
        product_size = request.POST.get('product_size')
        product_color = request.POST.get('product_color')

        if not product_name or not product_des or not product_catagory or not product_price or not product_sku:
            return render(request, 'complete_user_data.html', {'error': 'All required fields must be filled.'})

        # Create and save User_data object
        #print("ffffffff",vendors.shop_name)
        p_color = Color.objects.create(name = product_color)
        p_unit = Unit.objects.create(name = product_sku)
        p_size = Size.objects.create(name = product_size)
        p_catagory = Catagory.objects.create(name = product_catagory,parent_catagory_id=1)
        print("other print")   
        p_product  = Product.objects.create(
            title=product_name,
            details = product_des,
            shop_id = vendors,
            catagory_id= p_catagory,
            slug_product="http://www.goo45gl89e.com"
        )

        return redirect('home')
    
    return render(request, 'vendor_product_last.html',{'vendors': vendors,"user_vendor":user_vendor})
@login_required
def vendor_product_varient(request): 
    final_product_v=Product_varient.objects.all()
    final_product_v_number = len(final_product_v)
    vp_color = Color.objects.all()
    vp_unit = Unit.objects.all()
    vp_size = Size.objects.all()
    vp_catagory = Catagory.objects.all()
    vp_product = Product.objects.get(id=1)
    vp_vendors = Vendor.objects.get(id=1)
    
  
    if request.method == "POST":
        print("post mathod print")
        #user = request.user  # Get the currently logged-in user
        product_name = request.POST.get('product_name')
        product_des = request.POST.get('product_des')
        product_image = request.FILES.get('product_image')
        product_catagory = request.POST.get('product_catagory')
        product_price = request.POST.get('product_price')
        product_sku = request.POST.get('product_sku')
        product_size = request.POST.get('product_size')
        product_color = request.POST.get('product_color')
        product_quantity = request.POST.get('product_quantity')
        
        if not product_name or not product_des or not product_catagory or not product_price or not product_sku:
            return render(request, 'complete_user_data.html', {'error': 'All required fields must be filled.'})
       
        # Create and save User_data object
        #print("ffffffff",vendors.shop_name)
        verient_color = Color.objects.get(name = product_color)
        verient_unit = Unit.objects.get(name = product_sku)
        verient_size = Size.objects.get(name = product_size)
        verient_catagory = Catagory.objects.get(name=product_catagory)
        print("other print") 
        
        vp_product_varient = Product_varient.objects.create(
            title_pv=product_name,
            details = product_des,
            slug_pv = "http://www.googlebd.com",
            Total_stock = product_quantity,
            price=product_price,
            catagory_id = verient_catagory,
            product_id = vp_product,
            shop_id = vp_vendors,
            size_id = verient_size,
            color_id = verient_color,
            unit_id=verient_unit
        )
        pv_image = Product_image.objects.create(url=product_image,product_varient_id=vp_product_varient)
        
        return redirect('vendorVeriant')
    
    return render(request, 'vendor_verient_product.html',{"final_product_v":final_product_v,"vp_unit":vp_unit,"vp_color":vp_color,"vp_size":vp_size,"vp_catagory":vp_catagory,"final_product_v_number":final_product_v_number})


@login_required
def vendor_product_order(request):
    order_item = Order_items.objects.all()
    return render(request,"vendor_product_order.html",{"order_item":order_item})


@login_required
def review_and_rating(request,id=None):
    if request.method == "POST":
        comment = request.POST.get('comments')
        rate = request.POST.get('rating')
        product_v = Product_varient.objects.get(id=id)
        vendor_v = Vendor.objects.get(id=1)
        
        review_rate  = Review_and_rating.objects.create(
            customar_id=request.user,
            product_varient_id=product_v,
            vendor_id=vendor_v,
            rating=rate,
            review=comment
        )
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return JsonResponse({"error": "Invalid request"}, status=400)