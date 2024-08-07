# Generated by Django 4.2 on 2024-07-03 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0007_rename_registrodenuncia_denuncia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='estado',
            field=models.IntegerField(choices=[[0, 'En revisión'], [1, 'En procedimiento'], [2, 'Finalizada'], [3, 'Rechazada'], [4, 'Deshabilitada']], default=0, verbose_name='Estado de la denuncia'),
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
