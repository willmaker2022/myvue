# Generated by Django 3.2.9 on 2022-04-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productplan', '0030_auto_20220210_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processelprepare',
            options={'ordering': ('-updated',), 'verbose_name_plural': '电路板准备'},
        ),
        migrations.AddField(
            model_name='processelprepare',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
