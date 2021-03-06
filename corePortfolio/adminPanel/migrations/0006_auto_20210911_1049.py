# Generated by Django 3.2.7 on 2021-09-11 17:49

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0005_education_studyarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='LangSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(default='', max_length=100)),
                ('skill2', models.CharField(default='', max_length=100)),
                ('skill3', models.CharField(default='', max_length=100)),
                ('skill4', models.CharField(default='', max_length=100)),
                ('skill5', models.CharField(default='', max_length=100)),
                ('skill6', models.CharField(default='', max_length=100)),
                ('skill7', models.CharField(default='', max_length=100)),
                ('skill8', models.CharField(default='', max_length=100)),
                ('lang1', models.CharField(default='', max_length=100)),
                ('lang2', models.CharField(default='', max_length=100)),
                ('lang3', models.CharField(default='', max_length=100)),
                ('Icon1', models.ImageField(default='', upload_to='LangSkill/langIcons')),
                ('Icon2', models.ImageField(default='', upload_to='LangSkill/langIcons')),
                ('Icon3', models.ImageField(default='', upload_to='LangSkill/langIcons')),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='Nationality',
            field=django_countries.fields.CountryField(max_length=746, multiple=True),
        ),
    ]
