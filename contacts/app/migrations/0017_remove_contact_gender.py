# Generated by Django 2.2.1 on 2020-02-22 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200221_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='gender',
        ),
    ]