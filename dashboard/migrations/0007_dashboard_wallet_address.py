# Generated by Django 4.0.1 on 2022-05-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_dashboard_approved_deposit_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='wallet_address',
            field=models.CharField(default='this is the wallet address', max_length=300),
            preserve_default=False,
        ),
    ]