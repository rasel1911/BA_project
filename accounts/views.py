# accounts/views.py
#from django.shortcuts import render, redirect, HttpResponse
#from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.db import connection
#from .models import User
#from .forms import LoginForm
#from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import User_data,Address
from product.models import Product_image,Product_varient
from order_section.models import Card
from groq import Groq
from blog.models import Chat

client = Groq(
    api_key=config("api_key"),
)

@login_required
def chatbot_response(request):
    cha = Chat.objects.all()
    if request.POST:
        chat_text = request.POST.get("chat_bot")
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": chat_text+"give answer in summary",
            }
        ],
        model="llama-3.3-70b-versatile",stream=False,) 
                      
        chat=chat_completion.choices[0].message.content
        print(chat)
        c = Chat.objects.create(
            user_id = request.user,
            send=chat_text,
            recive= chat,
        )
        return redirect("home")
    return cha




"""
users=User.objects.all()
for user in users:
    print(user.name, user.password)
"""
@login_required
def calculate_price(request):
    cart_qpu = Card.objects.filter(customar_id=request.user)
    total_price = 0
    for i in cart_qpu:
        total_price = total_price+i.quantity*i.product_varient_id.price
    return total_price


def home_views(request):        
    
    product_varient_iamge = Product_image.objects.all()
    products = Product_varient.objects.all()
    
    try:
        card_number  = len(Card.objects.filter(customar_id=request.user))
        total_price = calculate_price(request)
    except:
        card_number="?"
        total_price=0
    print(card_number)
    ch=chatbot_response(request)
    ch = Chat.objects.filter()
    return render(request, 'home.html',{"product_varient_iamge":product_varient_iamge,"card_number":card_number,"total_price":total_price,"ch":ch})


"""
def register(request):
    if request.method == 'POST':
        name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        my_user=User(name=name,email=email,password=password)
        my_user.save()
    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(email=email)
                if user.password == password:  # Use Django authentication for security
                    request.session['user_id'] = user.id  # Store session manually
                    messages.success(request, "Login successful")
                    print(user.name)
                    return redirect('home')  # Redirect to home or dashboard
                else:
                    messages.error(request, "password invalid!!")
            except User.DoesNotExist:
                messages.error(request, "User not found")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
"""

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login page

    return render(request, 'sign_up_last.html')

"""
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)  # Django's built-in login
                messages.success(request, "Login successful")
                return redirect('home')  # Redirect to home or dashboard
            else:
                messages.error(request, "Invalid email or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

"""
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("pass1")
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        print(user.username,user.email)
        if user is not None:
            login(request, user)  # Django's built-in login
            messages.success(request, "Login successful")
            return redirect('home')  # Redirect to home or dashboard
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'sign_in_last.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('home')



def Contact(request):
    return render(request, 'contact.html')
"""
@login_required
def Complete_user_data(request):
    user = request.user  # Get the logged-in user
    print(user.id)
    f_username=user.username
    f_email=user.email
    f_password = user.password
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("pass1")
        
        
    return render(request, 'complete_user_data.html')
"""
'''
@login_required
def Complete_user_data(request):
    if request.method == "POST":
        user = request.user  # Get the currently logged-in user
        phone_no = request.POST['phone_no']
        type_user = request.POST['type_user']
        profile_image = request.FILES.get('profile_image')
        division = request.POST['division']
        city  = request.POST['city']
        zip_code = request.POST['zip_code']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        type_address = request.POST['type_address']

        # Create and save User_data object
        user_data = User_data.objects.create(
            user=user,  # Assign logged-in user
            phone_no=phone_no,
            type_user=type_user,
            profile_image=profile_image
        )
        customar_id=user_data.id
        
        user_address = Address.objects.create(
            division = division,
            city = city,
            zip_code = zip_code,
            address1 = address1,
            address2 = address2,
            type_address = type_address,
            customar_id = customar_id
        )
        
        return redirect('home')  # Redirect to some profile page

    return render(request, 'complete_user_data.html')
    
'''

@login_required
def Complete_user_data(request):
    if request.method == "POST":
        user = request.user  # Get the currently logged-in user
        phone_no = request.POST.get('phone_no')
        type_user = request.POST.get('type_user')
        profile_image = request.FILES.get('profile_image')
        division = request.POST.get('division')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        type_address = request.POST.get('type_address')

        if not phone_no or not type_user or not division or not city or not zip_code or not address1 or not type_address:
            return render(request, 'complete_user_data.html', {'error': 'All required fields must be filled.'})

        # Create and save User_data object
        user_data= User_data.objects.create(
            user=user,
            phone_no=phone_no,
            type_user=type_user,
            profile_image=profile_image
        )
        
        # Ensure we reference the User_data object correctly
        Address.objects.create(
            division=division,
            city=city,
            zip_code=zip_code,
            address_line1=address1,
            address_line2=address2,
            type_address=type_address,
            customar_id=user_data  # Correct reference to User_data instance
        )

        return redirect('home')  # Redirect to home or another appropriate page

    return render(request, 'complete_user_data.html')
