# Generated by Django 3.2.7 on 2021-09-16 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0016_user_registration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_Registration',
        ),
    ]