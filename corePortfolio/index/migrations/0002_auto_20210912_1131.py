# Generated by Django 3.2.7 on 2021-09-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(default='', max_length=100)),
                ('yourSubject', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Sayhello',
        ),
    ]
