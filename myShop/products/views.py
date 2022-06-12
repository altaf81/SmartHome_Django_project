from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import Phone, CartItem, Cart, Category


def index(req):
    page_obj = None
    categories = Category.get_all_categories()
    categoryId = req.GET.get('category')
    if categoryId:
        page_obj = Phone.get_all_products_by_categoryid(categoryId)
    else:
        products = Phone.objects.all()
        paginator = Paginator(products, 6)
        page_number = req.GET.get('page')
        page_obj = paginator.get_page(page_number)
    data = {}
    data['page_obj'] = page_obj
    data['categories'] = categories
    return render(req, 'home.html', data)


def about(req):
    return render(req, 'about.html')


class ProductDetailView(DetailView):
    model = Phone
    template_name = 'product.html'


def about(req):
    return render(req, 'about.html')


def contact(req):
    return render(req, 'contact.html')


def checkout(req):
    return render(req, 'checkout-page.html')


def search(req):
    query = req.GET['query']
    product = Phone.objects.filter(phoneName__icontains=query)
    context = {'product': product, 'query': query}
    return render(req, 'search.html', context)


def query(req):
    return render(req, 'query.html')


def placed(req):
    return render(req, 'placed.html')


@login_required
def add_to_cart(req, phoneId):
    cart, status = Cart.objects.get_or_create(user=req.user)
    phone = Phone.objects.get(phoneId=phoneId)
    item, created = CartItem.objects.get_or_create(phone=phone)
    if cart.itemlist.filter(id=item.id).exists():
        item.quantity = item.quantity + 1
        item.save()
        messages.info(req, 'This product quantity was updated')
        return redirect("products:viewcart")
    else:
        cart.itemlist.add(item)
        messages.info(req, 'This product was added to your cart')
        return redirect("products:viewcart")


@login_required
def viewcart(req):
    cart, status = Cart.objects.get_or_create(user=req.user)
    context = {'cart': cart}
    return render(req, 'viewcart.html', context)


@login_required
def removeitem(req, pk):
    item = CartItem.objects.get(pk=pk)
    item.delete()
    messages.success(req, f"{item.phone.phoneName} is remove from Cart")
    return redirect("products:viewcart")


@login_required
def updatecart(req):
    id = int(req.GET['id'])
    quantity = int(req.GET['quantity'])
    item = CartItem.objects.filter(pk=id)
    item.update(quantity=quantity)
    return HttpResponse(f"{item[0].phone.phoneName} is updated with {item[0].quantity} Quantity...")
