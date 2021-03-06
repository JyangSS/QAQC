from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import *


# =========PROJECT============================
class Company(models.Model):

    company = models.CharField(default=True, max_length=55, blank=True,null=False)

    def __str__(self):
        return str(self.company)



    pass


class Project(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    company_id = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)
    project_description = models.CharField(max_length=100,verbose_name="Project Description")
    project_short_form = models.CharField(max_length=10,verbose_name="Project Short Name")
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
        return str(self.company_id.company+"--  "+self.project_description)

    pass


class Phase(models.Model):
    class Meta:
        verbose_name = 'Phase'
        verbose_name_plural = 'Phases'

    project_id = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    phase_description = models.CharField(max_length=50)
    phase_short_form = models.CharField(max_length=10)
    inspection_object=models.CharField(max_length=2,unique=True,null=True)
    is_active = models.BooleanField(null=True)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField(null=True)
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.project_id.project_short_form + " ---  " + self.phase_short_form)

    pass


class UnitNumber(models.Model):
    class Meta:
        verbose_name = 'UnitNumber'
        verbose_name_plural = 'UnitsNumber'

    phase_id = models.ForeignKey(Phase, verbose_name="Phase", on_delete=models.CASCADE)
    block = models.CharField(max_length=2)
    level = models.IntegerField()
    unit_number = models.IntegerField()
    inspection_object = models.CharField(max_length=11)
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
'''
class InspectionObject(models.Model):
    class Meta:
        verbose_name = 'InspectionObject'
        verbose_name_plural = 'InspectionObjects'

    object_code = models.CharField(max_length=50)
    object_name = models.CharField(max_length=50)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.object_code)

    pass
'''