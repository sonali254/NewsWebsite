# Generated by Django 3.1.5 on 2021-01-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20210123_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='picname',
            field=models.TextField(),
        ),
    ]
