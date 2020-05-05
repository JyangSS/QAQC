# Generated by Django 3.0.4 on 2020-04-10 15:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, default=True, max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_description', models.CharField(max_length=50)),
                ('phase_short_form', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(null=True)),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField(null=True)),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Phase',
                'verbose_name_plural': 'Phases',
            },
        ),
        migrations.CreateModel(
            name='UnitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=10)),
                ('level', models.IntegerField()),
                ('unit_number', models.IntegerField()),
                ('inspection_object', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(null=True)),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField(null=True)),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
                ('phase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Phase', verbose_name='Phase')),
            ],
            options={
                'verbose_name': 'UnitNumber',
                'verbose_name_plural': 'UnitsNumber',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_description', models.CharField(max_length=100, verbose_name='Project Description')),
                ('project_short_form', models.CharField(max_length=10, verbose_name='Project Short Name')),
                ('location', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(null=True)),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField(null=True)),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AddField(
            model_name='phase',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Project', verbose_name='Project'),
        ),
    ]
