# Generated by Django 4.2.7 on 2023-12-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_initial_deposite_date_userbankaccount_initial_deposit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbankaccount',
            name='is_bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]