# Generated by Django 5.0.1 on 2024-01-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
