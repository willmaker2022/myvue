# Generated by Django 3.2.9 on 2021-11-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productplan', '0018_auto_20211123_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processassemble',
            options={'verbose_name_plural': '装配中'},
        ),
        migrations.AlterModelOptions(
            name='processelprepare',
            options={'verbose_name_plural': '电路板准备'},
        ),
        migrations.AlterModelOptions(
            name='processmeprepare',
            options={'verbose_name_plural': '机械件准备'},
        ),
        migrations.AlterModelOptions(
            name='processscprepare',
            options={'verbose_name_plural': '干涉仪准备'},
        ),
        migrations.AlterModelOptions(
            name='processtesting',
            options={'verbose_name_plural': '测试中'},
        ),
        migrations.AlterModelOptions(
            name='productplan',
            options={'verbose_name_plural': '订单管理'},
        ),
        migrations.AlterField(
            model_name='processassemble',
            name='status',
            field=models.CharField(choices=[('pending', '未开始'), ('process', '进行中'), ('finish', '已完成')], default='pending', max_length=10, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='processelprepare',
            name='status',
            field=models.CharField(choices=[('pending', '未开始'), ('process', '进行中'), ('finish', '已完成')], default='pending', max_length=10, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='processmeprepare',
            name='status',
            field=models.CharField(choices=[('pending', '未开始'), ('process', '进行中'), ('finish', '已完成')], default='pending', max_length=10, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='processscprepare',
            name='status',
            field=models.CharField(choices=[('pending', '未开始'), ('process', '进行中'), ('finish', '已完成')], default='pending', max_length=10, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='processtesting',
            name='status',
            field=models.CharField(choices=[('pending', '未开始'), ('process', '进行中'), ('finish', '已完成')], default='pending', max_length=10, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='status',
            field=models.CharField(choices=[('pending', '未开始'), ('process', '进行中'), ('finish', '已完成')], default='pending', max_length=10, verbose_name='订单状态'),
        ),
    ]
