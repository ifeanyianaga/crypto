# Generated by Django 4.0.1 on 2022-04-22 11:03

import django.core.validators
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_dashboard_comparator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='approved_deposit_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD Dollar')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='approved_withdrawal_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD Dollar')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='balance_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD Dollar')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='comparator_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD Dollar')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='earnings_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD Dollar')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='notification_deposit',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='notification_withdrawal',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='pending_deposit_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD Dollar')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='pending_withdrawal_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD Dollar')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='history',
            name='amount_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD Dollar')], default='USD', editable=False, max_length=3),
        ),
    ]
