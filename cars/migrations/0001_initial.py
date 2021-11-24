# Generated by Django 3.2.9 on 2021-11-25 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TirePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'tire_positions',
            },
        ),
        migrations.CreateModel(
            name='Tire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveSmallIntegerField()),
                ('aspect_ratio', models.PositiveSmallIntegerField()),
                ('wheel_size', models.PositiveSmallIntegerField()),
                ('tire_position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.tireposition')),
            ],
            options={
                'db_table': 'tires',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=32)),
                ('front_tire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='front_cars', to='cars.tire')),
                ('rear_tire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rear_cars', to='cars.tire')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
