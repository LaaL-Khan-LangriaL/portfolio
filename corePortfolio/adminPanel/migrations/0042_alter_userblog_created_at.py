# Generated by Django 3.2.9 on 2021-11-12 18:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0041_auto_20211112_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 18, 24, 55, 162553, tzinfo=utc)),
        ),
    ]