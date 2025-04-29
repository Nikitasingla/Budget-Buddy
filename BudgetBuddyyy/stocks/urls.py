from django.urls import path
from stocks import views

urlpatterns=[
    path('',views.homed,name='home'),
    path('stocked/', views.stock_list, name='stock_list'),
    path('add-to-cart/<int:stock_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
     path('cart/delete/<int:item_id>/', views.delete_from_cart, name='delete_from_cart')
]