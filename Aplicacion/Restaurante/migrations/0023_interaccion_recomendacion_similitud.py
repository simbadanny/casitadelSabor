# Generated by Django 3.2.25 on 2024-08-09 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0022_auto_20240809_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Similitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similitud', models.FloatField()),
                ('fecha_calculo', models.DateField(auto_now_add=True)),
                ('usuario1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similitudes_usuario1', to='Restaurante.clientes')),
                ('usuario2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similitudes_usuario2', to='Restaurante.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.FloatField()),
                ('fecha_recomendacion', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurante.clientes')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurante.menus')),
            ],
        ),
        migrations.CreateModel(
            name='Interaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurante.clientes')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurante.menus')),
            ],
        ),
    ]
