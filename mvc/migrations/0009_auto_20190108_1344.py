# Generated by Django 2.0 on 2019-01-08 05:44

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0008_auto_20190108_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='message',
            field=tinymce.models.HTMLField(verbose_name='消息'),
        ),
    ]