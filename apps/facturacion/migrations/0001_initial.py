# Generated by Django 5.1.1 on 2024-10-18 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detalles', '0001_initial'),
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='detalles.detallepedido')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedido.pedido')),
            ],
        ),
    ]
