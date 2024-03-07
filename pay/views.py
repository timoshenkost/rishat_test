import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from pay.models import Item, Order

STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    item_info = {
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': item.price,
    }

    return render(request, 'item.html', {'item': item_info})


def buy(request, id):
    item = get_object_or_404(Item, id=id)

    intent = stripe.PaymentIntent.create(
        amount=int(item.price * 100),
        currency='usd',
        description=item.name,
        payment_method_types=['card']
    )

    return render(request, 'confirm.html', {'item_price': item.price,
                                            'client_secret': intent.client_secret,
                                            'stripe_key': STRIPE_PUBLIC_KEY})


def order_detail(request, slug):
    order = get_object_or_404(Order, slug=slug)
    order_info = {
        'slug': order.slug,
        'items': order.items.all(),
        'name': order.name,
        'description': order.description,
    }

    return render(request, 'order.html', {'order': order_info, 'stripe_key': STRIPE_PUBLIC_KEY})


def buy_order(request, slug):
    order = get_object_or_404(Order, slug=slug)
    total_price = int(sum(item.price for item in order.items.all()))
    taxes = [tax.tax_rate_id for tax in order.taxes.all()]
    coupon = order.discount.coupon_id if order.discount else None

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': order.name,
                    'description': order.description
                },
                'unit_amount': total_price * 100,
            },
            'quantity': 1,
            'tax_rates': taxes,
        }],
        discounts=[{'coupon': coupon}],
        mode='payment',
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:8000/cancel',
    )

    return JsonResponse({'id': session.id})
