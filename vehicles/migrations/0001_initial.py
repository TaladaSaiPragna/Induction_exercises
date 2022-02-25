# Generated by Django 4.0.1 on 2022-02-25 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lp_number', models.CharField(max_length=10, unique=True)),
                ('wheel_count', models.IntegerField(max_length=9)),
                ('manufacturer', models.CharField(max_length=25)),
                ('model_name', models.CharField(max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.vehicle')),
                ('is_air_conditioned', models.BooleanField()),
                ('has_roof_top', models.BooleanField()),
            ],
            bases=('vehicles.vehicle',),
        ),
        migrations.CreateModel(
            name='truck',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.vehicle')),
                ('max_goods_weight', models.IntegerField(max_length=1000)),
                ('docfile', models.FileField(default=None, upload_to='documents/%Y/%m/%d')),
            ],
            bases=('vehicles.vehicle',),
        ),
    ]
