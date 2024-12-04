from django.shortcuts import render, redirect
from django.http import HttpResponse
from carts.models import CartItem
from .forms import OrderForm
import datetime
from .models import Order, OrderProduct
from store.models import Product
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from main_page.context_data import get_common_context, get_page_context


def place_order(request, total=0, quantity=0):
    current_user = request.user

    # If the cart count is less than or equal to 0, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store:all_product_list')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price() * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total) / 100
    # whitout tax
    tax = 0
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside the Order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")  # 20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)

            # Move the cart items to Order Product table
            ordered_products = []
            for item in cart_items:
                orderproduct = OrderProduct()
                orderproduct.order_id = order.id
                orderproduct.user_id = request.user.id
                orderproduct.product_id = item.product_id
                orderproduct.quantity = item.quantity
                orderproduct.product_price = item.product.price()
                orderproduct.ordered = True
                orderproduct.save()

                ordered_products.append(orderproduct)

                # Reduce the quantity of the sold products
                product = Product.objects.get(id=item.product_id)
                product.available_quantity -= item.quantity
                product.save()

            # Clear cart
            CartItem.objects.filter(user=request.user).delete()

            # Send order received email to customer
            mail_subject = 'Thank you for your order!'
            message = render_to_string('orders/order_recieved_email.html', {
                'user': request.user,
                'order': order,
            })
            to_email = request.user.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            data = {
                'order': order,
                'order_number': order.order_number,
                'ordered_products': ordered_products,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }
            context_req = get_page_context(request)
            context_data = get_common_context()
            data.update(context_data)
            data.update(context_req)
            return render(request, 'orders/order_complete.html', context=data)
        else:
            # Handle invalid form submissions
            return render(request, 'store/checkout.html', {'form': form, 'cart_items': cart_items, 'total': total, 'tax': tax, 'grand_total': grand_total})

    return redirect('cart:checkout')
