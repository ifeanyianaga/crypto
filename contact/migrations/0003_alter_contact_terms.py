# Generated by Django 4.0.1 on 2022-04-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_situation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='terms',
            field=models.BooleanField(verbose_name='Accepted the terms'),
        ),
    ]