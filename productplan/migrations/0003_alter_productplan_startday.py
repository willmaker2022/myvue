# Generated by Django 3.2.9 on 2021-11-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productplan', '0002_auto_20211122_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productplan',
            name='startday',
            field=models.DateField(auto_now_add=True, verbose_name='下单时间'),
        ),
    ]