# Generated by Django 4.1 on 2022-09-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_alter_pessoas_dizimista_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoas',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='img/usuarios/'),
        ),
    ]
