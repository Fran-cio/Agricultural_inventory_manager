# Generated by Django 5.0.1 on 2024-01-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_view', '0002_sujeto_cuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sujeto',
            name='cuit',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
