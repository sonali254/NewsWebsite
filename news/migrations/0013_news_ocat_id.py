# Generated by Django 3.1.5 on 2021-01-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_news_cat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ocat_id',
            field=models.IntegerField(default=0),
        ),
    ]
