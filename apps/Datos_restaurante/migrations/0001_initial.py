# Generated by Django 5.1.1 on 2024-10-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_restaurante', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='logos/')),
            ],
        ),
    ]
