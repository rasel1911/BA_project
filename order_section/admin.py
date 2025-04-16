from django.contrib import admin

# Register your models here.

from .models import Card, Whitelist , Order , Order_address , Order_items, Order_status, Payment

admin.site.register(Card)
admin.site.register(Whitelist)
admin.site.register(Order)
admin.site.register(Order_address)
admin.site.register(Order_items)
admin.site.register(Order_status)
admin.site.register(Payment)