# Generated by Django 4.2.3 on 2023-07-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('destination', models.CharField(max_length=100)),
                ('budget', models.CharField(max_length=50)),
            ],
        ),
    ]
