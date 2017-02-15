# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=20)),
                ('dept_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('salary', models.IntegerField(default=2000)),
                ('phone_number', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_salary', models.CharField(max_length=100)),
                ('max_salary', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=35)),
                ('employ_id', models.ForeignKey(to='human.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('city', models.CharField(max_length=300, serialize=False, primary_key=True)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organization_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('organization_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='location_id',
            field=models.ForeignKey(to='human.Organization'),
        ),
        migrations.AddField(
            model_name='department',
            name='employ_id',
            field=models.ForeignKey(to='human.Employee'),
        ),
    ]
