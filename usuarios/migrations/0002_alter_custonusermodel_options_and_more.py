# Generated by Django 4.1 on 2022-08-27 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custonusermodel',
            options={},
        ),
        migrations.AlterModelTable(
            name='custonusermodel',
            table='usuarios',
        ),
    ]
