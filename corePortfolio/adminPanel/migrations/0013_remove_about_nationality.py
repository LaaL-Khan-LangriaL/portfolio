# Generated by Django 3.2.7 on 2021-09-12 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0012_socialmedia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='Nationality',
        ),
    ]
