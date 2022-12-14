# Generated by Django 4.1.3 on 2022-11-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=8),
        ),
    ]
