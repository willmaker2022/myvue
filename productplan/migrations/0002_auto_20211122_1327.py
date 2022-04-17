# Generated by Django 3.2.9 on 2021-11-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productplan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productplan',
            name='customer',
            field=models.CharField(max_length=20, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='endday',
            field=models.DateField(verbose_name='交货时间'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='orderid',
            field=models.CharField(max_length=10, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='productid',
            field=models.CharField(max_length=10, verbose_name='产品型号'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='serial',
            field=models.CharField(max_length=10, verbose_name='序列号'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='startday',
            field=models.DateField(auto_now=True, verbose_name='下单时间'),
        ),
    ]
