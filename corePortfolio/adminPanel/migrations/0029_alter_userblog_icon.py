# Generated by Django 3.2.9 on 2021-11-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0028_alter_userblog_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='Icon',
            field=models.ImageField(default='', upload_to='Blog/Icons'),
        ),
    ]
