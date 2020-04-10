from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import *


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
    description = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    creator_user_id = models.CharField(max_length=50, blank=True)
    last_modification_time = models.DateTimeField(null=True, blank=True)
    last_modifier_user_id = models.CharField(max_length=50, blank=True)
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(null=True, blank=True)
    delete_user_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.element)

    pass


class Group(models.Model):
    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    element_id = models.ForeignKey(Element, on_delete=models.CASCADE)
    defect_group = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    creator_user_id = models.CharField(max_length=50, blank=True)
    last_modification_time = models.DateTimeField(null=True, blank=True)
    last_modifier_user_id = models.CharField(max_length=50, blank=True)
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(null=True, blank=True)
    delete_user_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.element_id) + ' - ' + str(self.defect_group)

    pass


# =========InspectionForm================================


class NumberSeries(models.Model):
    class Meta:
        verbose_name = 'NumberSeries'
        verbose_name_plural = 'Number_Series'

    series = models.CharField(max_length=50)
    current = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    creator_user_id = models.CharField(max_length=50, blank=True)
    last_modification_time = models.DateTimeField(null=True, blank=True)
    last_modifier_user_id = models.CharField(max_length=50, blank=True)
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(null=True, blank=True)
    delete_user_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.series)

    pass


class FormTypeTemplate(models.Model):
    class Meta:
        verbose_name = 'FormTypeTemplate'
        verbose_name_plural = 'FormTypeTemplates'

    number_series_id = models.ForeignKey(NumberSeries, on_delete=models.CASCADE)
    form_type = models.CharField(max_length=20)
    form_description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    creator_user_id = models.CharField(max_length=50, blank=True)
    last_modification_time = models.DateTimeField(null=True, blank=True)
    last_modifier_user_id = models.CharField(max_length=50, blank=True)
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(null=True, blank=True)
    delete_user_id = models.CharField(max_length=50, blank=True)

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
    rev = models.IntegerField(default=1)
    remarks = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    creator_user_id = models.CharField(max_length=50, blank=True)
    last_modification_time = models.DateTimeField(null=True, blank=True)
    last_modifier_user_id = models.CharField(max_length=50, blank=True)
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(null=True, blank=True)
    delete_user_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.form_title)

    pass


class TemplateDetail(models.Model):
    class Meta:
        verbose_name = 'TemplateDetail'
        verbose_name_plural = 'TemplateDetails'

    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    form_template_id = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    legend = models.CharField(max_length=5)
    question_line = models.IntegerField()
    question = models.CharField(max_length=500)
    is_boolean_question = models.BooleanField(null=False)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    creator_user_id = models.CharField(max_length=50, blank=True)
    last_modification_time = models.DateTimeField(null=True, blank=True)
    last_modifier_user_id = models.CharField(max_length=50, blank=True)
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(null=True, blank=True)
    delete_user_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.question)

    pass


class Inspection01(models.Model):
    class Meta:
        verbose_name = 'Inspection1'
        verbose_name_plural = 'Inspections1'

    form_template_id = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    unit_number_id = models.ForeignKey('objects.UnitNumber', on_delete=models.CASCADE)
    inspection_count=models.IntegerField(null=True)   # for count the reinspection form
    draw_ref = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    creator_user_id = models.CharField(max_length=50, blank=True)
    last_modification_time = models.DateTimeField(null=True, blank=True)
    last_modifier_user_id = models.CharField(max_length=50, blank=True)
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(null=True, blank=True)
    delete_user_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)

    pass


class Inspection02(models.Model):
    class Meta:
        verbose_name = 'Inspection2'
        verbose_name_plural = 'Inspections2'

    inspection_01_id = models.ForeignKey(Inspection01, on_delete=models.CASCADE)
    contractor = models.CharField(max_length=10,null=True)
    consultant = models.CharField(max_length=10,null=True)
    consultant_reinspection = models.CharField(max_length=10,null=True)
    inspection = models.CharField(max_length=10,null=True)
    reason = models.CharField(max_length=200,null=True)
    comment = RichTextUploadingField(null=True)
    accept = models.BooleanField(null=True)
    accept_date = models.DateTimeField(default=datetime.now, blank=True,null=True)
    contractor_name = models.CharField(max_length=50,null=True)
    contractor_date = models.DateTimeField(default=datetime.now, blank=True,null=True)
    consultant_name = models.CharField(max_length=50,null=True)
    consultant_date = models.DateTimeField(default=datetime.now, blank=True,null=True)
    remarks = RichTextUploadingField()
    is_active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    creator_user_id = models.CharField(max_length=50, blank=True)
    last_modification_time = models.DateTimeField(null=True, blank=True)
    last_modifier_user_id = models.CharField(max_length=50, blank=True)
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(null=True, blank=True)
    delete_user_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)

    pass
