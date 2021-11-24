# Generated by Django 3.2.9 on 2021-11-12 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0040_auto_20211112_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='userblog',
            name='quote_by',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 11, 43, 48, 34358, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='quote',
            field=models.CharField(default='', max_length=3000),
        ),
    ]