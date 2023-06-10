# Generated by Django 4.0.1 on 2022-04-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_alter_crypto_logo_svg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
                ('testimony', models.TextField(max_length=150)),
                ('country', models.CharField(max_length=250)),
            ],
        ),
    ]
