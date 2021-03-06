# Generated by Django 2.2.1 on 2020-02-21 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200221_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number_plate',
            field=models.CharField(default=None, max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='number_plate',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Contact', to_field='number_plate'),
        ),
    ]
