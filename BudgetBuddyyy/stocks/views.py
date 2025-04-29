from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from mainpage.views import register_view,login_view,logout_view

# Create your views here.

def homed(request):
    return render(request,'home.html')

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock, CartItem

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stock_list.html', {'stocks': stocks})

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Stock, CartItem

@login_required
def add_to_cart(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    item, created = CartItem.objects.get_or_create(user=request.user, stock=stock)

    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    grand_total = sum(item.get_total_price() for item in items)
    return render(request, 'cart.html', {'items': items, 'grand_total': grand_total})
@login_required
def delete_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart_view')



