# Generated by Django 5.2 on 2025-04-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_consulta_medico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
