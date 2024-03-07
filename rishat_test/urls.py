from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from pay.views import buy, item_detail, order_detail, buy_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:id>/', buy, name='buy'),
    path('item/<int:id>/', item_detail, name='item'),
    path('order/<slug:slug>/', order_detail, name='order'),
    path('buy_order/<slug:slug>/', buy_order, name='buy_order'),
    path('success/', TemplateView.as_view(template_name='success.html')),
]
