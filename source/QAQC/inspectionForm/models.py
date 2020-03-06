from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import *


# =========PROJECT============================
class Project(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    project_description = models.CharField(max_length=100)
    project_short_form = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.project_short_form)

    pass


class Phase(models.Model):
    class Meta:
        verbose_name = 'Phase'
        verbose_name_plural = 'Phases'

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    phase_description = models.CharField(max_length=50)
    phase_short_form = models.CharField(max_length=10)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.phase_short_form)

    pass


class UnitNumber(models.Model):
    class Meta:
        verbose_name = 'UnitNumber'
        verbose_name_plural = 'UnitsNumber'

    phase_id = models.ForeignKey(Phase, on_delete=models.CASCADE)
    block = models.CharField(max_length=10)
    level = models.IntegerField(max_length=5)
    unit_number = models.CharField(max_length=10)
    inspection_object = models.CharField(max_length=50)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.block + "-" + self.level + "-" + self.unit_number)

    pass


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


# =========DETAIL============================
class Element(models.Model):
    class Meta:
        verbose_name = 'Element'
        verbose_name_plural = 'Elements'

    element = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.element)

    pass


class Group(models.Model):
    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    element_id = models.ForeignKey(Element, on_delete=models.CASCADE)
    defect_group = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.defect_group)

    pass

#=========InspectionForm================================
class NumberSeries(models.Model):
    class Meta:
        verbose_name = 'NumberSeries'
        verbose_name_plural = 'Number_Series'

    series = models.IntegerField(max_length=5)
    current = models.IntegerField(max_length=5)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    pass


class FormTypeTemplate(models.Model):
    class Meta:
        verbose_name = 'FormTypeTemplate'
        verbose_name_plural = 'FormTypeTemplates'

    number_series_id = models.ForeignKey(NumberSeries, on_delete=models.CASCADE)
    form_type = models.CharField(max_length=20)
    form_description = models.CharField(max_length=200)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.form_type)

    pass


class FormTemplate(models.Model):
    class Meta:
        verbose_name = 'FormTemplate'
        verbose_name_plural = 'FormTemplates'

    form_type_template_id = models.ForeignKey(FormTypeTemplate, on_delete=models.CASCADE)
    form_title = models.CharField(max_length=200)
    ref_no = models.CharField(max_length=20)
    remarks = models.CharField(max_length=200)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    pass


class TemplateDetail(models.Model):
    class Meta:
        verbose_name = 'TemplateDetail'
        verbose_name_plural = 'TemplateDetails'

    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    form_template_id = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    legend = models.CharField(max_length=5)
    question_line = models.IntegerField(max_length=15)
    question = models.CharField(max_length=500)
    is_boolean_question = models.BooleanField()
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    pass


class Inspection01(models.Model):
    class Meta:
        verbose_name = 'Inspection1'
        verbose_name_plural = 'Inspections1'

    template_detail_id = models.ForeignKey(TemplateDetail, on_delete=models.CASCADE)
    unit_number_id = models.ForeignKey(UnitNumber, on_delete=models.CASCADE)
    rev = models.IntegerField(max_length=3)
    draw_ref = models.CharField(max_length=15)
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    pass


class Inspection02(models.Model):
    class Meta:
        verbose_name = 'Inspection2'
        verbose_name_plural = 'Inspections2'

    inspection_01_id = models.ForeignKey(Inspection01, on_delete=models.CASCADE)
    contractor = models.CharField(max_length=10)
    consultant = models.CharField(max_length=10)
    consultant_reinspection = models.CharField(max_length=10)
    inspection = models.CharField(max_length=10)
    reason = models.CharField(max_length=200)
    comment = RichTextUploadingField()
    accept = models.BooleanField()
    accept_date = models.DateTimeField(default=datetime.now, blank=True)
    contractor_name = models.CharField(max_length=50)
    contractor_date = models.DateTimeField(default=datetime.now, blank=True)
    consultant_name = models.CharField(max_length=50)
    consultant_date = models.DateTimeField(default=datetime.now, blank=True)
    remarks = RichTextUploadingField()
    is_active = models.BooleanField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id = models.CharField(max_length=50)
    last_modification_time = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    deletion_time = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    pass
