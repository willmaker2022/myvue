# Generated by Django 3.2.9 on 2022-02-13 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productplan', '0030_auto_20220210_1643'),
        ('storage', '0033_alter_storage_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='InOutStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('in', '入库'), ('out', '出库')], default='out', max_length=5, verbose_name='操作方向')),
                ('lCount', models.IntegerField(default=0, verbose_name='数量')),
                ('operateday', models.DateTimeField(verbose_name='操作日期')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_inout', to='productplan.productplan')),
                ('storage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='storage_inout', to='storage.storage')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_inout', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '出入库记录',
                'ordering': ('-operateday',),
            },
        ),
    ]