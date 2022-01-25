# Generated by Django 2.2.24 on 2022-01-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transport',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
