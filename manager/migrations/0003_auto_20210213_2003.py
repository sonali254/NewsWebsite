# Generated by Django 3.1.6 on 2021-02-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20210203_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.TextField(default='.'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='manager',
            name='utxt',
            field=models.TextField(),
        ),
    ]
