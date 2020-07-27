# Generated by Django 3.0.6 on 2020-06-17 03:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0026_auto_20200617_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='half_bathrooms',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(models.PositiveIntegerField())], verbose_name='1/2 Bathroom'),
        ),
        migrations.AlterField(
            model_name='home',
            name='heating_system1',
            field=models.CharField(choices=[('Forced Air (gas)', 'Forced Air (gas)'), ('Electric', 'Electric'), ('Geothermal', 'Geothermal'), ('Radiant Heat', 'Radiant Heat'), ('Steam Radiant Heat', 'Steam Radiant Heat'), (None, 'None')], default='Electric', max_length=50, null=True, verbose_name='Main Heating'),
        ),
        migrations.AlterField(
            model_name='home',
            name='heating_system2',
            field=models.CharField(choices=[('Forced Air (gas)', 'Forced Air (gas)'), ('Electric', 'Electric'), ('Geothermal', 'Geothermal'), ('Radiant Heat', 'Radiant Heat'), ('Steam Radiant Heat', 'Steam Radiant Heat'), (None, 'None')], default='None', max_length=50, null=True, verbose_name='Secondary Heating'),
        ),
        migrations.AlterField(
            model_name='home',
            name='one_quarter_bathrooms',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(models.PositiveIntegerField())], verbose_name='1/4 Bathroom'),
        ),
    ]