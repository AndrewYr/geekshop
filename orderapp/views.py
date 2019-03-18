from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from basketapp.models import Basket
from .models import Order, ProductInOrder

@user_passes_test(lambda u: u.is_superuser)
def order(request):
    basket = Basket.objects.filter(user=request.user)
    text_message = ''
    new_order_item = Order(user=request.user)
    new_order_item.save()

    for item in basket:
        new_product_item = ProductInOrder(order=new_order_item, product=item.product, quantity=item.quantity)
        new_product_item.save()

        text_message += 'Товар id ' + str(item.product.id) + ' в количестве ' + str(item.quantity) + '\n'
        item.delete()
    sendmessage(request.user, text_message)

    return render(request, 'basketapp/basket.html', locals())

def order_add(request, basket):
    return render(request, 'basketapp/basket.html', locals())

def sendmessage(user, text_message):

    send_mail('Заказ от {}'.format(user.email), text_message, 'Человек<{}>'.format(settings.SENDER_EMAIL), ['test@mail.ru'])