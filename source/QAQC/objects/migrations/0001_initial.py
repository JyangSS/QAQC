# Generated by Django 3.0.3 on 2020-03-17 10:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(choices=[('Johor', 'Johor'), ('Kuala Lumpur', 'Kuala Lumpur'), ('Penang', 'Penang')], default=True, max_length=55)),
                ('project_description', models.CharField(max_length=100)),
                ('project_short_form', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
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
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='UnitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=10)),
                ('level', models.IntegerField()),
                ('unit_number', models.CharField(max_length=10)),
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
        migrations.AddField(
            model_name='phase',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Project', verbose_name='Project'),
        ),
    ]
