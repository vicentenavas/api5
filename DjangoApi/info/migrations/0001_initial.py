# Generated by Django 4.2.2 on 2023-06-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servizio',
            fields=[
                ('servizioId', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descrizione', models.CharField(max_length=100)),
                ('imgUrl', models.CharField(max_length=100)),
                ('siOcuppa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('socioId', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=25)),
                ('info', models.CharField(max_length=70)),
            ],
        ),
    ]
