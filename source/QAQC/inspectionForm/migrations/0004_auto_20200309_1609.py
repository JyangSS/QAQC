# Generated by Django 3.0.3 on 2020-03-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspectionForm', '0003_auto_20200309_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.CharField(max_length=100, verbose_name='Project'),
        ),
    ]
