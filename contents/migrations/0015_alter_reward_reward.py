# Generated by Django 4.0.1 on 2022-04-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0014_bounty_background_color_bounty_heading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='reward',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
