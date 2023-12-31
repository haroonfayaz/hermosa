# Generated by Django 4.1.7 on 2023-07-10 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=3555)),
                ('image_url', models.CharField(max_length=2083)),
            ],
            options={
                'db_table': 'Destination',
            },
        ),
        migrations.CreateModel(
            name='TravelBud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(10)])),
                ('travel_date', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('adult', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('children', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'Travelers',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='travel_date',
            field=models.DateField(null=True),
        ),
    ]
