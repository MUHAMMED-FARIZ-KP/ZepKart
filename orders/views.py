from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from products.models import Product
# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)


def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)

        # Try to find an existing ordered item with the same product and cart
        ordered_item_qs = OrderedItem.objects.filter(product=product, owner=cart_obj)

        if ordered_item_qs.exists():
            # If an item already exists, update its quantity
            ordered_item = ordered_item_qs.first()
            ordered_item.quantity += quantity
            ordered_item.save()
        else:
            # If no such item exists, create a new one
            ordered_item = OrderedItem.objects.create(
                product=product,
                owner=cart_obj,
                quantity=quantity
            )
            
    return redirect('cart')
