# Generated by Django 3.2.9 on 2021-12-11 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0022_auto_20211211_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lendstorage',
            name='sName',
        ),
    ]
