# Generated by Django 3.1.4 on 2020-12-27 14:52

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainWebsite', '0002_auto_20201224_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='Post Content', null=True),
        ),
    ]
