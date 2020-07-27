# Generated by Django 3.0.6 on 2020-06-17 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0027_auto_20200617_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='attached_garage',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='Yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='home',
            name='heating_system2',
            field=models.CharField(choices=[('Forced Air (gas)', 'Forced Air (gas)'), ('Electric', 'Electric'), ('Geothermal', 'Geothermal'), ('Radiant Heat', 'Radiant Heat'), ('Steam Radiant Heat', 'Steam Radiant Heat'), (None, 'None')], default='None', max_length=50, null=True, verbose_name='Other Heating'),
        ),
        migrations.AlterField(
            model_name='home',
            name='master_bathroom',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='Yes', max_length=10, verbose_name='Master Bathroom?'),
        ),
        migrations.AlterField(
            model_name='home',
            name='master_bedroom',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='Yes', max_length=10, verbose_name='Master Bedroom?'),
        ),
        migrations.AlterField(
            model_name='home',
            name='new_construction',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='No', max_length=10),
        ),
    ]
