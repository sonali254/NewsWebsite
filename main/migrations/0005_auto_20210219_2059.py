# Generated by Django 3.1.6 on 2021-02-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_main_abouttxt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='picname',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='picname2',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='picurl',
            field=models.TextField(default='.', null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='picurl2',
            field=models.TextField(default='.', null=True),
        ),
    ]
