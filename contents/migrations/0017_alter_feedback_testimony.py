# Generated by Django 4.0.1 on 2022-04-14 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0016_plan_withdrawal_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='testimony',
            field=models.TextField(max_length=250),
        ),
    ]