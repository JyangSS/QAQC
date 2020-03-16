from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import *


# =========PROJECT============================
class Project(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    company_choice = [
        ('Johor', 'Johor'),
        ('Kuala Lumpur', 'Kuala Lumpur'),
        ('Penang', 'Penang'),
    ]
    company = models.CharField(max_length=55, choices=company_choice, default=None)
    project_description = models.CharField(max_length=100)
    project_short_form = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(null=True)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField(null=True)
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.company + "--    " + self.project_description)

    pass


class Phase(models.Model):
    class Meta:
        verbose_name = 'Phase'
        verbose_name_plural = 'Phases'

    project_id = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    phase_description = models.CharField(max_length=50)
    phase_short_form = models.CharField(max_length=10)
    is_active = models.BooleanField(null=True)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField(null=True)
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.project_id.project_description + "--  " + self.phase_description)

    pass


class UnitNumber(models.Model):
    class Meta:
        verbose_name = 'UnitNumber'
        verbose_name_plural = 'UnitsNumber'

    phase_id = models.ForeignKey(Phase, verbose_name="Phase", on_delete=models.CASCADE)
    block = models.CharField(max_length=10)
    level = models.IntegerField()
    unit_number = models.CharField(max_length=10)
    inspection_object = models.CharField(max_length=50)
    is_active = models.BooleanField(null=True)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField(null=True)
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.block + "-" + str(self.level) + "-" + self.unit_number)

    pass
