from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm

from cart.models import Cart, CartItem
from catering.models import CateringProduct
from cart.views import _cart_id


def order_create(request, total=0):

    order_form = OrderCreateForm()
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, active=True)

    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order_form = order_form.save()

            for cart_item in cart_items:

                order_item = OrderItem.objects.create(
                    order=order_form,
                    product=cart_item.product,
                    price=cart_item.product.price,
                    quantity=cart_item.quantity
                )
                order_item.save()

                # Reduce stock
                product = CateringProduct.objects.get(slug=cart_item.product.slug)
                product.stock = int(cart_item.product.stock - cart_item.quantity)
                product.save()

                cart_item.delete()

        return render(request, 'creation_order_success.html')

    return render(request, 'create_order.html', {
        'form': order_form,
        'cart_items': cart_items,
        'total': total
    })
