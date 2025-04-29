from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Stock, CartItem

admin.site.register(Stock)
admin.site.register(CartItem)
