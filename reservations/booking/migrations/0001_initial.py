# Generated by Django 4.2 on 2024-04-22 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure_depart', models.DateTimeField()),
                ('heure_arrivee', models.DateTimeField()),
                ('gare_arrivee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gare_arrivee', to='booking.gare')),
                ('gare_depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gare_depart', to='booking.gare')),
            ],
        ),
    ]