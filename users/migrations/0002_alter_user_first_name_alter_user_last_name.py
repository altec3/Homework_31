# Generated by Django 4.1.3 on 2022-11-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default=None, help_text='Имя. Максимум 20 символов', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default=None, help_text='Фамилия. Максимум 50 символов', max_length=50),
        ),
    ]
