# Generated by Django 3.2.9 on 2021-11-10 11:23

import ckeditor5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0022_userblog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='description',
            field=ckeditor5.fields.RichTextField(default=''),
        ),
    ]
