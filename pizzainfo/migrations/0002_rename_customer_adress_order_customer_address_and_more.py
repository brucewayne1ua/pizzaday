# Generated by Django 4.1 on 2024-06-19 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzainfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_adress',
            new_name='customer_address',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='aviability',
            new_name='availability',
        ),
    ]
