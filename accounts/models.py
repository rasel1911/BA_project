from django.db import models
"""
# Create your models here.
class User_data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15, unique=True)
    last_login_at = models.DateTimeField(auto_now=True)
    email_verified_at = models.DateField(auto_now_add=True)
    type_user= models.CharField(max_length=25)
    profile_image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified
"""
from django.contrib.auth.models import User  # Import Django's built-in User model

class User_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # ForeignKey to User model
    phone_no = models.CharField(max_length=15, unique=True) 
    last_login_at = models.DateTimeField(auto_now=True)
    email_verified_at = models.DateField(auto_now_add=True)
    type_user = models.CharField(max_length=25)
    profile_image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time modified

    def __str__(self):
        return self.user.username  # Return the username of the linked User

class Vendor(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    slug =  models.URLField(max_length=500, unique=True, null=True) 
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    tradelicense = models.CharField(max_length=255, unique=True)
    rating=  models.IntegerField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    customar_id = models.ForeignKey(User_data, on_delete=models.CASCADE)
    division = models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    zip_code = models.IntegerField()
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    type_address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)