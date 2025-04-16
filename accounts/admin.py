from django.contrib import admin

# Register your models here.

from .models import User_data, Vendor, Address

admin.site.register(User_data)
admin.site.register(Vendor)
admin.site.register(Address)