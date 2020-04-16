# Generated by Django 3.0.4 on 2020-04-17 01:04

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.CharField(error_messages={'unique': 'Element already exist.'}, max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('creator_user_id', models.CharField(blank=True, max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, null=True)),
                ('last_modifier_user_id', models.CharField(blank=True, max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_time', models.DateTimeField(blank=True, null=True)),
                ('delete_user_id', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Element',
                'verbose_name_plural': 'Elements',
            },
        ),
        migrations.CreateModel(
            name='FormTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_title', models.CharField(error_messages={'unique': 'Form title already exist.'}, max_length=200, unique=True)),
                ('ref_no', models.CharField(max_length=20)),
                ('rev', models.IntegerField(default=1)),
                ('remarks', models.CharField(blank=True, max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('creator_user_id', models.CharField(blank=True, max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, null=True)),
                ('last_modifier_user_id', models.CharField(blank=True, max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_time', models.DateTimeField(blank=True, null=True)),
                ('delete_user_id', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'FormTemplate',
                'verbose_name_plural': 'FormTemplates',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defect_group', models.CharField(error_messages={'unique': 'Group already exist.'}, max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('creator_user_id', models.CharField(blank=True, max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, null=True)),
                ('last_modifier_user_id', models.CharField(blank=True, max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_time', models.DateTimeField(blank=True, null=True)),
                ('delete_user_id', models.CharField(blank=True, max_length=50)),
                ('element_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.Element')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Inspection01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_count', models.IntegerField(null=True)),
                ('inspection', models.CharField(max_length=25, null=True)),
                ('draw_ref', models.CharField(max_length=15, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('creator_user_id', models.CharField(blank=True, max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, null=True)),
                ('last_modifier_user_id', models.CharField(blank=True, max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_time', models.DateTimeField(blank=True, null=True)),
                ('delete_user_id', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Inspection1',
                'verbose_name_plural': 'Inspections1',
            },
        ),
        migrations.CreateModel(
            name='NumberSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(error_messages={'unique': 'Series name already exist.'}, max_length=50, unique=True)),
                ('current', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('creator_user_id', models.CharField(blank=True, max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, null=True)),
                ('last_modifier_user_id', models.CharField(blank=True, max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_time', models.DateTimeField(blank=True, null=True)),
                ('delete_user_id', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'NumberSeries',
                'verbose_name_plural': 'Number_Series',
            },
        ),
        migrations.CreateModel(
            name='TemplateDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legend', models.CharField(blank=True, max_length=5, null=True)),
                ('question_line', models.IntegerField(blank=True, null=True)),
                ('question', models.CharField(max_length=500)),
                ('is_boolean_question', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('creator_user_id', models.CharField(blank=True, max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, null=True)),
                ('last_modifier_user_id', models.CharField(blank=True, max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_time', models.DateTimeField(blank=True, null=True)),
                ('delete_user_id', models.CharField(blank=True, max_length=50)),
                ('form_template_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.FormTemplate')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.Group')),
            ],
            options={
                'verbose_name': 'TemplateDetail',
                'verbose_name_plural': 'TemplateDetails',
            },
        ),
        migrations.CreateModel(
            name='Inspection02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200, null=True)),
                ('comment', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('accept', models.BooleanField(null=True)),
                ('accept_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('contractor_name', models.CharField(max_length=50, null=True)),
                ('contractor_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('consultant_name', models.CharField(max_length=50, null=True)),
                ('consultant_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('remarks', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('creator_user_id', models.CharField(blank=True, max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, null=True)),
                ('last_modifier_user_id', models.CharField(blank=True, max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_time', models.DateTimeField(blank=True, null=True)),
                ('delete_user_id', models.CharField(blank=True, max_length=50)),
                ('inspection01_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.Inspection01')),
            ],
            options={
                'verbose_name': 'Inspection02',
                'verbose_name_plural': 'Inspections02',
            },
        ),
        migrations.AddField(
            model_name='inspection01',
            name='template_detail_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.TemplateDetail'),
        ),
        migrations.AddField(
            model_name='inspection01',
            name='unit_number_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.UnitNumber'),
        ),
        migrations.CreateModel(
            name='FormTypeTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_type', models.CharField(error_messages={'unique': 'Form type already exist.'}, max_length=20, unique=True)),
                ('form_description', models.CharField(error_messages={'unique': 'Short Name already exist.'}, max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('creator_user_id', models.CharField(blank=True, max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, null=True)),
                ('last_modifier_user_id', models.CharField(blank=True, max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_time', models.DateTimeField(blank=True, null=True)),
                ('delete_user_id', models.CharField(blank=True, max_length=50)),
                ('number_series_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.NumberSeries')),
            ],
            options={
                'verbose_name': 'FormTypeTemplate',
                'verbose_name_plural': 'FormTypeTemplates',
            },
        ),
        migrations.AddField(
            model_name='formtemplate',
            name='form_type_template_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.FormTypeTemplate'),
        ),
    ]
