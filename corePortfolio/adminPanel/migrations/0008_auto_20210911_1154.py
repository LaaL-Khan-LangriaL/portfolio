# Generated by Django 3.2.7 on 2021-09-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0007_auto_20210911_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='langskill',
            name='expert1',
            field=models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='langskill',
            name='expert2',
            field=models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='langskill',
            name='expert3',
            field=models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='langskill',
            name='expert4',
            field=models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='langskill',
            name='expert5',
            field=models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='langskill',
            name='expert6',
            field=models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='langskill',
            name='expert7',
            field=models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='langskill',
            name='expert8',
            field=models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100),
        ),
    ]
