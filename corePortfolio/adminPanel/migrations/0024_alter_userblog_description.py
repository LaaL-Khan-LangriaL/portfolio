# Generated by Django 3.2.9 on 2021-11-10 11:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0023_alter_userblog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]