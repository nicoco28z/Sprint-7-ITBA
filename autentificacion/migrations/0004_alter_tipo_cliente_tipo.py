# Generated by Django 4.2.7 on 2023-11-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentificacion', '0003_tipo_cliente_alter_customuser_dni_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_cliente',
            name='tipo',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
