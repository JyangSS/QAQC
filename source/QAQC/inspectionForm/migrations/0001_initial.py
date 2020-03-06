# Generated by Django 3.0.3 on 2020-03-06 15:27

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
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
                ('form_title', models.CharField(max_length=200)),
                ('ref_no', models.CharField(max_length=20)),
                ('remarks', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
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
                ('defect_group', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
                ('element_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.Element')),
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
                ('rev', models.IntegerField(max_length=3)),
                ('draw_ref', models.CharField(max_length=15)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Inspection1',
                'verbose_name_plural': 'Inspections1',
            },
        ),
        migrations.CreateModel(
            name='InspectionObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_code', models.CharField(max_length=50)),
                ('object_name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'InspectionObject',
                'verbose_name_plural': 'InspectionObjects',
            },
        ),
        migrations.CreateModel(
            name='NumberSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField(max_length=5)),
                ('current', models.IntegerField(max_length=5)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'NumberSeries',
                'verbose_name_plural': 'Number_Series',
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_description', models.CharField(max_length=50)),
                ('phase_short_form', models.CharField(max_length=10)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
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
                ('project_description', models.CharField(max_length=100)),
                ('project_short_form', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
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
                ('level', models.IntegerField(max_length=5)),
                ('unit_number', models.CharField(max_length=10)),
                ('inspection_object', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
                ('phase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.Phase')),
            ],
            options={
                'verbose_name': 'UnitNumber',
                'verbose_name_plural': 'UnitsNumber',
            },
        ),
        migrations.CreateModel(
            name='TemplateDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legend', models.CharField(max_length=5)),
                ('question_line', models.IntegerField(max_length=15)),
                ('question', models.CharField(max_length=500)),
                ('is_boolean_question', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
                ('form_template_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.FormTemplate')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.Group')),
            ],
            options={
                'verbose_name': 'TemplateDetail',
                'verbose_name_plural': 'TemplateDetails',
            },
        ),
        migrations.AddField(
            model_name='phase',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.Project'),
        ),
        migrations.CreateModel(
            name='Inspection02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor', models.CharField(max_length=10)),
                ('consultant', models.CharField(max_length=10)),
                ('consultant_reinspection', models.CharField(max_length=10)),
                ('inspection', models.CharField(max_length=10)),
                ('reason', models.CharField(max_length=200)),
                ('comment', ckeditor_uploader.fields.RichTextUploadingField()),
                ('accept', models.BooleanField()),
                ('accept_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('contractor_name', models.CharField(max_length=50)),
                ('contractor_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('consultant_name', models.CharField(max_length=50)),
                ('consultant_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('remarks', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
                ('inspection_01_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.Inspection01')),
            ],
            options={
                'verbose_name': 'Inspection2',
                'verbose_name_plural': 'Inspections2',
            },
        ),
        migrations.AddField(
            model_name='inspection01',
            name='template_detail_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.TemplateDetail'),
        ),
        migrations.AddField(
            model_name='inspection01',
            name='unit_number_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.UnitNumber'),
        ),
        migrations.CreateModel(
            name='FormTypeTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_type', models.CharField(max_length=20)),
                ('form_description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
                ('creation_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator_user_id', models.CharField(max_length=50)),
                ('last_modification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_modifier_user_id', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField()),
                ('deletion_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete_user_id', models.CharField(max_length=50)),
                ('number_series_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.NumberSeries')),
            ],
            options={
                'verbose_name': 'FormTypeTemplate',
                'verbose_name_plural': 'FormTypeTemplates',
            },
        ),
        migrations.AddField(
            model_name='formtemplate',
            name='form_type_template_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspectionForm.FormTypeTemplate'),
        ),
    ]
