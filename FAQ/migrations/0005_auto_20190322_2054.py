# Generated by Django 2.0 on 2019-03-22 11:54

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0004_auto_20190322_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=froala_editor.fields.FroalaField(),
        ),
    ]