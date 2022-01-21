# Generated by Django 2.2.24 on 2022-01-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_transport_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='transport_type',
            field=models.CharField(choices=[('Pick-Up', 'Pick-Up'), ('Delivery', 'Delivery')], default='Pick-Up', max_length=10),
        ),
    ]