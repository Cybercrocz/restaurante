# Generated by Django 5.1.1 on 2024-09-25 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tempo_preparo', models.IntegerField(help_text='Tempo de preparo em minutos')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pendente', max_length=20)),
                ('data_agendamento', models.DateTimeField(blank=True, null=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.produto')),
            ],
        ),
    ]
