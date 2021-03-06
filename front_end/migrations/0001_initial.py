# Generated by Django 4.0.3 on 2022-03-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Classe', models.CharField(max_length=30)),
                ('Ordem', models.CharField(max_length=30)),
                ('Familia', models.CharField(max_length=30)),
                ('Genero', models.CharField(max_length=30)),
                ('Especie', models.CharField(max_length=30)),
                ('Nome_Popular', models.CharField(max_length=30)),
                ('Data_da_coleta', models.CharField(max_length=30)),
                ('Hora_da_coleta', models.CharField(max_length=30)),
                ('Datum', models.CharField(max_length=30)),
                ('Coordenada_x', models.CharField(max_length=30)),
                ('Coordenada_y', models.CharField(max_length=30)),
                ('Metodo_de_coleta', models.CharField(max_length=30)),
                ('Tipo_de_registro', models.CharField(max_length=30)),
                ('Responsavel_pela_coleta', models.CharField(max_length=30)),
            ],
        ),
    ]
