# Generated by Django 3.2.9 on 2021-12-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_lendstorage'),
    ]

    operations = [
        migrations.AddField(
            model_name='lendstorage',
            name='idText',
            field=models.TextField(null=True),
        ),
    ]
