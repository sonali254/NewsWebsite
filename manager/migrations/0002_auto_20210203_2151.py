# Generated by Django 3.1.6 on 2021-02-03 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='uname',
            new_name='utxt',
        ),
    ]
