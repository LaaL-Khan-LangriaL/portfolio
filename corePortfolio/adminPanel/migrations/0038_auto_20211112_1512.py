# Generated by Django 3.2.9 on 2021-11-12 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0037_alter_userblog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 10, 12, 43, 674992, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='heading',
            field=models.CharField(default='', max_length=5000),
        ),
    ]