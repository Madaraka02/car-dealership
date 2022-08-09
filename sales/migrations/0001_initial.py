# Generated by Django 4.1 on 2022-08-09 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('condition', models.CharField(blank=True, max_length=100, null=True)),
                ('make', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=200, null=True)),
                ('mileage', models.CharField(blank=True, max_length=100, null=True)),
                ('engine_size', models.CharField(blank=True, max_length=100, null=True)),
                ('power', models.CharField(blank=True, max_length=100, null=True)),
                ('fuel', models.CharField(blank=True, max_length=100, null=True)),
                ('gearbox', models.CharField(blank=True, max_length=100, null=True)),
                ('doors', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_seats', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='cars/images')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='cars/images')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.vehicle')),
            ],
        ),
    ]
