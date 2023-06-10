# Generated by Django 4.0.1 on 2022-03-21 08:06

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='comparator',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('20.0'), default_currency='USD', max_digits=14, verbose_name='comparator'),
        ),
    ]
