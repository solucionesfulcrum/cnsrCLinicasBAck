# Generated by Django 3.1.1 on 2021-09-16 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDoc', models.CharField(max_length=30)),
                ('numDoc', models.CharField(max_length=10)),
                ('apePat', models.CharField(max_length=30)),
                ('apeMat', models.CharField(max_length=30)),
                ('nombres', models.CharField(max_length=50)),
                ('fechaNac', models.DateField(null=True)),
                ('sexo', models.CharField(max_length=15, null=True)),
                ('estado', models.CharField(default=1, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='presAnemia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPres', models.DateField(null=True)),
                ('nomNefro', models.CharField(max_length=30)),
                ('medPres', models.CharField(max_length=30)),
                ('dosisPres', models.IntegerField()),
                ('viaAdmPres', models.CharField(max_length=10)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CnsrPac.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='AdmiAnemia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAdmi', models.DateField(null=True)),
                ('nomEnfer', models.CharField(max_length=30)),
                ('medAdmi', models.CharField(max_length=30)),
                ('dosisAdmi', models.IntegerField()),
                ('viaAdm', models.CharField(max_length=10)),
                ('presAnemia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CnsrPac.presanemia')),
            ],
        ),
    ]
