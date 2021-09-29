# Generated by Django 3.1.1 on 2021-09-28 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CnsrPac', '0005_exclusionanemia'),
    ]

    operations = [
        migrations.CreateModel(
            name='movimientoAnemia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaMotivo', models.DateField()),
                ('razonMotivo', models.CharField(max_length=30)),
                ('obserMotivo', models.CharField(max_length=30)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CnsrPac.paciente')),
            ],
        ),
    ]