from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Admin)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
