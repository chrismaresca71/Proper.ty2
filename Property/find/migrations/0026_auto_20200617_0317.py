# Generated by Django 3.0.6 on 2020-06-17 03:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0025_home_master_bathroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='three_quarter_bathrooms',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(models.PositiveIntegerField())], verbose_name='3/4 Bathroom'),
        ),
    ]
