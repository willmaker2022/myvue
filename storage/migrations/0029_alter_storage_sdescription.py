# Generated by Django 3.2.9 on 2021-12-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0028_alter_storage_spartnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='sDescription',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='描述'),
        ),
    ]
