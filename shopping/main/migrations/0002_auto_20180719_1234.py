# Generated by Django 2.0.3 on 2018-07-19 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Login'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Login'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='customerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Login'),
        ),
    ]