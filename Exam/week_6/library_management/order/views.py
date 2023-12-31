from django.shortcuts import render, redirect
from .models import CartItem
from books.models import Book
 
def product_list(request):
    products = Book.objects.all()
    return render(request, 'index.html', {'products': products})

# Create your views here.
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.borrowing_price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Book.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.total_price = cart_item.product.borrowing_price * cart_item.quantity
    cart_item.save()
    product.save()
    return redirect('view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')