# Generated by Django 4.1.3 on 2022-11-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]