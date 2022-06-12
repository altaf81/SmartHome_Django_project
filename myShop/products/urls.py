from django.urls import path
from .views import (
    about,
    checkout,
    contact,
    search,
    query,
    placed,
    index,
    ProductDetailView,
    add_to_cart,
    viewcart,
    removeitem,
    updatecart
)

app_name = 'products'

urlpatterns = [
    path('', index, name='home'),
    path('product/<pk>/', ProductDetailView.as_view(), name='product'),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
    path('contact-us/', contact, name='contact-us'),
    path('query/', query, name='query'),
    path('checkout/', checkout, name='checkout'),
    path('order-placed/', placed, name='order-placed'),
    path('add-to-cart/<int:phoneId>/', add_to_cart, name='add-to-cart'),
    path("viewcart", viewcart, name="viewcart"),
    path('remove-from-cart/<int:pk>/', removeitem, name='remove-from-cart'),
    path("updatecart", updatecart, name="updatecart"),
]
