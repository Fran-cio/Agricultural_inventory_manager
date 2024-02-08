# Generated by Django 5.0.1 on 2024-01-09 15:45

# pylint: disable=duplicate-code,line-too-long

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulo_view', '0001_initial'),
        ('clientes_view', '0003_alter_sujeto_cuit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remitos_cliente', to='clientes_view.sujeto')),
                ('provedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remitos_proveedor', to='clientes_view.sujeto')),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo_view.articulo')),
                ('remito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remito_view.remito')),
            ],
        ),
    ]
