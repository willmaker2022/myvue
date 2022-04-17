# Generated by Django 3.2.9 on 2022-02-15 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productplan', '0030_auto_20220210_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='故障描述')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operator', to=settings.AUTH_USER_MODEL)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='productplan.productplan', verbose_name='订单号')),
            ],
            options={
                'verbose_name_plural': '维修记录',
                'ordering': ('-updated',),
            },
        ),
    ]
