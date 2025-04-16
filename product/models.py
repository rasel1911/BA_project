from django.db import models
from accounts.models import Vendor

# Create your models here.
class Size(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified

class Color(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified

class Unit(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified

class Catagory(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50)
    parent_catagory_id= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified


class Product(models.Model):
    title = models.CharField(max_length=255)
    catagory_id = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    details = models.TextField()
    slug_product =  models.URLField(max_length=500, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified

class Product_varient(models.Model):
    title_pv = models.CharField(max_length=255)
    catagory_id = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    details = models.TextField()
    slug_pv =  models.URLField(max_length=500, null=True) 
    Total_stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified

class Stock(models.Model):
    product_varient_id  = models.ForeignKey(Product_varient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified

class Product_image(models.Model):
    product_varient_id = models.ForeignKey(Product_varient, on_delete=models.CASCADE)
    url = models.ImageField(upload_to='images/')
    master_image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)  # Update every time the object is modified
