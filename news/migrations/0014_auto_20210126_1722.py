# Generated by Django 3.1.5 on 2021-01-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_news_ocat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]