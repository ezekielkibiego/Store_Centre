

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('booked', models.BooleanField(default=False)),
                ('charge', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage_type', models.CharField(max_length=100)),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('description', models.TextField(max_length=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to=settings.AUTH_USER_MODEL)),
                ('unit_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store', to='units.unit')),
            ],
        ),
    ]
