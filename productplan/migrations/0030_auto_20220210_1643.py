# Generated by Django 3.2.9 on 2022-02-10 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productplan', '0029_alter_producthistory_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producthistory',
            name='operateday',
            field=models.DateTimeField(null=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='producthistory',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_history', to='productplan.productplan', verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='producthistory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]