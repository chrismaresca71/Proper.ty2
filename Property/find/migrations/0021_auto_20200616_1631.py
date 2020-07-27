# Generated by Django 3.0.6 on 2020-06-16 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0020_auto_20200616_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='major_remodel_year',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2020)]),
        ),
    ]
