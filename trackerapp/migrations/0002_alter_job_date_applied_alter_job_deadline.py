# Generated by Django 4.2.21 on 2025-06-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_applied',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
