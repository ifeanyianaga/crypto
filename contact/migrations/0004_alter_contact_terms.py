# Generated by Django 4.0.1 on 2022-04-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='terms',
            field=models.BooleanField(default=False, verbose_name='Accepted the terms'),
        ),
    ]
