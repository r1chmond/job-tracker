# Generated by Django 4.2.21 on 2025-06-12 10:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, validators=[django.core.validators.RegexValidator(message='title must only be alphabets', regex='^[A-Za-z\\s]+$')])),
                ('company', models.CharField(max_length=500, validators=[django.core.validators.RegexValidator(message='company name cannot include symbols', regex='^[A-Za-z0-9\\s]+$')])),
                ('url', models.URLField(max_length=500)),
                ('location', models.CharField(max_length=500, validators=[django.core.validators.RegexValidator(message='location must only be alphabets', regex='^[A-Za-z\\s]+$')])),
                ('status', models.CharField(max_length=20)),
                ('date_applied', models.DateField(blank=True)),
                ('deadline', models.DateField(blank=True)),
                ('description', models.TextField()),
                ('date_time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_time_added'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('date_time_added', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackerapp.job')),
            ],
            options={
                'ordering': ['-date_time_added'],
            },
        ),
    ]
