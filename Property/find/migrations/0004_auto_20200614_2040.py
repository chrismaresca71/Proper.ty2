# Generated by Django 3.0.6 on 2020-06-14 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200613_0307'),
        ('find', '0003_address_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Agent'),
        ),
    ]
