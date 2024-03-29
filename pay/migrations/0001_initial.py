# Generated by Django 4.2.11 on 2024-03-07 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Скидка в процентах')),
                ('coupon_id', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Процент')),
                ('inclusive', models.BooleanField(verbose_name='Включен в стоимость')),
                ('tax_rate_id', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pay.discount', verbose_name='Скидка')),
                ('items', models.ManyToManyField(to='pay.item', verbose_name='Продукты')),
                ('taxes', models.ManyToManyField(blank=True, to='pay.tax', verbose_name='Налоги')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
