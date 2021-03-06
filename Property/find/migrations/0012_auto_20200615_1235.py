# Generated by Django 3.0.6 on 2020-06-15 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0011_auto_20200615_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='heating_system1',
            field=models.CharField(choices=[('Forced Air (gas)', 'Forced Air (gas)'), ('Electric', 'Electric'), ('Geothermal', 'Geothermal'), ('Radiant Heat', 'Radiant Heat'), ('Steam Radiant Heat', 'Steam Radiant Heat'), ('None', 'None')], default='Electric', max_length=50, null=True, verbose_name='Main Heating System'),
        ),
        migrations.AlterField(
            model_name='home',
            name='heating_system2',
            field=models.CharField(choices=[('Forced Air (gas)', 'Forced Air (gas)'), ('Electric', 'Electric'), ('Geothermal', 'Geothermal'), ('Radiant Heat', 'Radiant Heat'), ('Steam Radiant Heat', 'Steam Radiant Heat'), ('None', 'None')], default='None', max_length=50, null=True, verbose_name='Second Heating System'),
        ),
    ]
