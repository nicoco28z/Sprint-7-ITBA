# Generated by Django 4.2.7 on 2023-11-25 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='nro_cuenta',
        ),
    ]
