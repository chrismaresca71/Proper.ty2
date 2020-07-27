# Generated by Django 3.0.6 on 2020-06-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20200613_0302'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Financial',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='client',
            name='credit',
        ),
        migrations.AddField(
            model_name='client',
            name='cash_inv',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='credit_score',
            field=models.CharField(choices=[('< 700', '<700'), ('700 - 739', '700 - 739'), ('740 - 779', '740 - 779'), ('780 +', '780 +')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='household_income',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='high_price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='low_price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Credit',
        ),
    ]
