# Generated by Django 3.0.4 on 2020-04-07 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_auto_20200407_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitnumber',
            name='max_level',
        ),
        migrations.RemoveField(
            model_name='unitnumber',
            name='max_unit_per_level',
        ),
    ]