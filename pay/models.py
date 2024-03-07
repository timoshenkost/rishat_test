import stripe

from django.db import models
from django.urls import reverse
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class Item(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item', kwargs={'id': self.id})


class Discount(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    percent = models.DecimalField(verbose_name='Скидка в процентах', max_digits=5, decimal_places=2)
    coupon_id = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def save(self, *args, **kwargs):
        coupon = stripe.Coupon.create(percent_off=self.percent)
        self.coupon_id = coupon.id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    percentage = models.DecimalField(verbose_name='Процент', max_digits=5, decimal_places=2)
    inclusive = models.BooleanField(verbose_name='Включен в стоимость')
    tax_rate_id = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def save(self, *args, **kwargs):
        tax_rate = stripe.TaxRate.create(
            display_name=self.name,
            percentage=self.percentage,
            inclusive=self.inclusive
        )
        self.tax_rate_id = tax_rate.id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    items = models.ManyToManyField(Item, verbose_name='Продукты')
    description = models.TextField(verbose_name='Описание')

    discount = models.ForeignKey(Discount, verbose_name='Скидка', null=True, blank=True, on_delete=models.SET_NULL)
    taxes = models.ManyToManyField(Tax, verbose_name='Налоги', blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name
