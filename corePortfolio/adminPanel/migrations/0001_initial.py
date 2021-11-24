# Generated by Django 3.2.7 on 2021-09-07 16:46

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='', max_length=100)),
                ('Designation', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=100)),
                ('areaofResearch', models.CharField(default='', max_length=100)),
                ('previousJob', models.CharField(default='', max_length=100)),
                ('School', models.CharField(default='', max_length=100)),
                ('Birthday', models.CharField(default='', max_length=100)),
                ('meritalStatus', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='', max_length=100)),
                ('Nationality', django_countries.fields.CountryField(default='', max_length=2)),
                ('Skype', models.CharField(default='', max_length=100)),
                ('Phone', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(default='', max_length=254)),
                ('description', models.TextField(default='')),
                ('profile', models.ImageField(default='', upload_to='profiles')),
            ],
        ),
    ]
