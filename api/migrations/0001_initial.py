# Generated by Django 5.1.7 on 2025-03-21 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodavnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv_prodavnice', models.CharField(max_length=50)),
                ('lokacija_prodavnice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proizvod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv_prozvoda', models.CharField(max_length=50)),
                ('opis', models.TextField()),
                ('cena', models.DecimalField(decimal_places=2, max_digits=4)),
                ('prodavnica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prodavnica')),
            ],
        ),
    ]
