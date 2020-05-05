# Generated by Django 3.0.6 on 2020-05-05 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.Product')),
                ('shoppingCart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_cart_app.ShoppingCart')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='items',
            field=models.ManyToManyField(through='shopping_cart_app.ShoppingCartItem', to='store_app.Product'),
        ),
    ]
