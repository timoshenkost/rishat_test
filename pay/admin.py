from django.contrib import admin
from .models import Item, Order, Discount, Tax

admin.site.register(Item)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    exclude = ('tax_rate_id',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    exclude = ('coupon_id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
