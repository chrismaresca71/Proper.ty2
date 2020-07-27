# Generated by Django 3.0.6 on 2020-06-15 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0016_auto_20200615_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='attached_garage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='home',
            name='full_bathrooms',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(models.PositiveIntegerField())]),
        ),
        migrations.AddField(
            model_name='home',
            name='half_bathrooms',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(models.PositiveIntegerField())]),
        ),
        migrations.AddField(
            model_name='home',
            name='levels',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='home',
            name='master_bedrooom',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='home',
            name='new_construction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='home',
            name='one_quarter_bathrooms',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(models.PositiveIntegerField())]),
        ),
        migrations.AddField(
            model_name='home',
            name='parking_spcaes',
            field=models.PositiveIntegerField(default=2, null=True, validators=[django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AddField(
            model_name='home',
            name='pool',
            field=models.CharField(choices=[(None, 'None'), ('In-ground', 'In-ground'), ('Above Ground', 'Above Ground')], default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='home',
            name='stories',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='home',
            name='three_quarter_bathrooms',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(models.PositiveIntegerField())]),
        ),
    ]