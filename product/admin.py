from django.contrib import admin

# Register your models here.
from .models import Size,Color,Catagory,Unit,Product,Product_varient,Product_image,Stock

admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Catagory)
admin.site.register(Unit)
admin.site.register(Product)
admin.site.register(Product_varient)
admin.site.register(Product_image)
admin.site.register(Stock)

