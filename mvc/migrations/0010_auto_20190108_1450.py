# Generated by Django 2.0 on 2019-01-08 06:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0009_auto_20190108_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='message',
            field=tinymce.models.HTMLField(),
        ),
    ]
