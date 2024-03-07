# Generated by Django 5.0.3 on 2024-03-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_alter_item_options_alter_item_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
