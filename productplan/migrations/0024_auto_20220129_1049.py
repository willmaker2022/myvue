# Generated by Django 3.2.9 on 2022-01-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productplan', '0023_auto_20220129_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processassemble',
            name='endday',
            field=models.DateField(null=True, verbose_name='交货时间'),
        ),
        migrations.AlterField(
            model_name='processelprepare',
            name='endday',
            field=models.DateField(null=True, verbose_name='交货时间'),
        ),
        migrations.AlterField(
            model_name='processmeprepare',
            name='endday',
            field=models.DateField(null=True, verbose_name='交货时间'),
        ),
        migrations.AlterField(
            model_name='processscprepare',
            name='endday',
            field=models.DateField(null=True, verbose_name='交货时间'),
        ),
        migrations.AlterField(
            model_name='processtesting',
            name='endday',
            field=models.DateField(null=True, verbose_name='交货时间'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='endday',
            field=models.DateField(null=True, verbose_name='交货时间'),
        ),
    ]
