# Generated by Django 4.0.1 on 2022-04-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0015_alter_reward_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='withdrawal_period',
            field=models.CharField(max_length=300, null=True),
        ),
    ]