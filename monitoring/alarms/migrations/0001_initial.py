# Generated by Django 3.2.6 on 2024-05-04 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('limitExceeded', models.FloatField(blank=True, default=None, null=True)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.solicitud')),
            ],
        ),
    ]