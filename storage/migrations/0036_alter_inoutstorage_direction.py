# Generated by Django 3.2.9 on 2022-03-23 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0035_auto_20220214_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inoutstorage',
            name='direction',
            field=models.CharField(choices=[('in', '入库'), ('out', '出库'), ('buyin', '采购')], default='out', max_length=5, verbose_name='操作方向'),
        ),
    ]