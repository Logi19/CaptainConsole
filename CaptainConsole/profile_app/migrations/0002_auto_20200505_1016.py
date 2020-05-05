# Generated by Django 3.0.6 on 2020-05-05 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_app', '0001_initial'),
        ('shopping_cart_app', '0001_initial'),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='searchProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.Product'),
        ),
        migrations.AddField(
            model_name='searchhistory',
            name='searchProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='searches',
            field=models.ManyToManyField(through='profile_app.SearchHistory', to='store_app.Product'),
        ),
        migrations.AddField(
            model_name='profile',
            name='shoppingCart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_cart_app.ShoppingCart'),
        ),
        migrations.AddField(
            model_name='address',
            name='postal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.Postal'),
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.Profile'),
        ),
    ]
