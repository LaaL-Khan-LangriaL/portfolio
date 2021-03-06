# Generated by Django 3.2.7 on 2021-09-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0009_auto_20210911_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=300)),
                ('thumbnail', models.ImageField(default='', upload_to='Portfolio/Thumbnails')),
            ],
        ),
    ]
