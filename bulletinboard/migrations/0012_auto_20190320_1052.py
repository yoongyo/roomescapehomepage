# Generated by Django 2.0 on 2019-03-20 01:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bulletinboard', '0011_auto_20190318_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletinboard',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]