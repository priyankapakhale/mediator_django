# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-25 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediator_app', '0013_auto_20180125_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMedicine',
            fields=[
                ('user_med_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('expiry_date', models.DateField()),
                ('use', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=100)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediator_app.Medicine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediator_app.User')),
            ],
        ),
    ]
