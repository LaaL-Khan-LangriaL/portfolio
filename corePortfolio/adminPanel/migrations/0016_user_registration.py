# Generated by Django 3.2.7 on 2021-09-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0015_auto_20210912_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(default='', max_length=100)),
                ('Email', models.EmailField(default='', max_length=100)),
                ('Password', models.CharField(default='', max_length=100)),
                ('cnfPassword', models.CharField(default='', max_length=100)),
            ],
        ),
    ]