# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_url', models.CharField(max_length=125)),
                ('job_comp', models.CharField(max_length=125)),
                ('job_name', models.CharField(max_length=125)),
                ('job_smoney', models.IntegerField(max_length=125)),
                ('job_emoney', models.IntegerField(max_length=125)),
                ('job_address', models.CharField(max_length=125)),
                ('job_comp_type', models.CharField(max_length=125)),
                ('job_comp_snum', models.IntegerField(max_length=125)),
                ('job_comp_enum', models.IntegerField(max_length=125)),
                ('job_business', models.CharField(max_length=125)),
                ('job_syear', models.IntegerField(max_length=125)),
                ('job_eyear', models.IntegerField(max_length=125)),
                ('job_date_pub', models.CharField(max_length=125)),
                ('job_datetime', models.CharField(max_length=125)),
                ('job_welfafe', models.CharField(max_length=125)),
                ('job_people', models.CharField(max_length=125)),
                ('job_desc', models.CharField(max_length=125)),
                ('job_request', models.CharField(max_length=125)),
                ('job_tag', models.CharField(max_length=125)),
                ('job_degree', models.CharField(max_length=125)),
            ],
            options={
                'db_table': 'job',
            },
        ),
    ]