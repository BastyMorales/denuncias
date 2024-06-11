# Generated by Django 4.2.13 on 2024-06-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_registrodenuncia_alter_geolocation_report_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrodenuncia',
            name='causa',
            field=models.IntegerField(choices=[[0, 'Lugar de explotación'], [1, 'Uso y/o contaminación de recursos naturales'], [2, 'Residuos, emisiones e inmisiones']], verbose_name='Causa de conflicto'),
        ),
    ]
