# Generated by Django 3.1.5 on 2021-01-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210123_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.CharField(default='.', max_length=30),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic',
            field=models.CharField(default='.', max_length=30),
        ),
    ]