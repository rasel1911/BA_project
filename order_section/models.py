from django.db import models
from accounts.models import User_data , Vendor
from product.models import Product_varient
from django.contrib.auth.models import User
# Create your models here.

class Whitelist(models.Model):
    customar_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_varient_id = models.ForeignKey(Product_varient , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)

class Card(models.Model):
    customar_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_varient_id = models.ForeignKey(Product_varient , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    customar_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    customar_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=25)
    type  = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)

class Order_status(models.Model):
    customar_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=25)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)

class Order_address(models.Model):
    customar_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    division = models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    zip_code = models.IntegerField()
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    type_address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)
    
class Order_items(models.Model):
    customar_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product_varient_id = models.ForeignKey(Product_varient, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cupon = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)
    
class Review_and_rating(models.Model):
    customar_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_varient_id = models.ForeignKey(Product_varient, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)