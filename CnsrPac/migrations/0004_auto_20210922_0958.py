# Generated by Django 3.1.1 on 2021-09-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CnsrPac', '0003_auto_20210922_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='admianemia',
            name='viaAdmHierro',
            field=models.CharField(default=3, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presanemia',
            name='viaAdmHiePres',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
