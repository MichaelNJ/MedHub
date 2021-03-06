# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_fname', models.CharField(max_length=30)),
                ('patient_mname', models.CharField(max_length=30)),
                ('patient_sname', models.CharField(max_length=30)),
                ('patient_id', models.IntegerField()),
                ('patient_age', models.IntegerField()),
                ('patient_email', models.EmailField(max_length=254)),
                ('time', models.DateTimeField()),
                ('patient_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='current_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reception.Year'),
        ),
    ]
