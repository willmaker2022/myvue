# Generated by Django 3.2.9 on 2022-03-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0036_alter_inoutstorage_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inoutstorage',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage_inout', to='storage.storage'),
        ),
    ]
