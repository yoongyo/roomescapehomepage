# Generated by Django 2.0 on 2019-03-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0007_auto_20190314_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='people1',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='people2',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='people3',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='people4',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='people5',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='people6',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
