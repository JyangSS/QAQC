from django.db import models
from django.urls import reverse
from datetime import datetime

#=========PROJECT============================
class Project(models.Model):
    project_description     = models.CharField(max_length=100)
    project_short_form      = models.CharField(max_length=10)
    location                = models.CharField(max_length=100)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class Phase(models.Model):
    project_id              = models.ForeignKey(Project, on_delete=models.CASCADE)
    phase_description       = models.CharField(max_length=50)
    phase_short_form        = models.CharField(max_length=10)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class UnitNumber(models.Model):
    phase_id                = models.ForeignKey(Phase, on_delete=models.CASCADE)
    block                   = models.CharField(max_length=10)
    level                   = models.IntegerField(max_length=5)
    unit_number             = models.CharField(max_length=10)
    inspection_object       = models.CharField(max_length=50)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class InspectionObject(models.Model):
    object_code             = models.CharField(max_length=50)
    object_name             = models.CharField(max_length=50)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass
#=========DETAIL============================
class Element(models.Model):
    element                 = models.CharField(max_length=50)
    description             = models.CharField(max_length=200)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class Group(models.Model):
    element_id              = models.ForeignKey(Element, on_delete=models.CASCADE)
    defect_group            = models.CharField(max_length=100)
    description             = models.CharField(max_length=200)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class NumberSeries(models.Model):
    current                 = models.IntegerField(max_length=5)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class FormTypeTemplate(models.Model):
    number_series_id        = models.ForeignKey(NumberSeries, on_delete=models.CASCADE)
    form_type               = models.CharField(max_length=20)
    form_description        = models.CharField(max_length=200)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class FormTemplate(models.Model):
    form_type_template_id   = models.ForeignKey(FormTypeTemplate, on_delete=models.CASCADE)
    form_title              = models.CharField(max_length=200)
    ref_no                  = models.CharField(max_length=20)
    remarks                 = models.CharField(max_length=200)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class TemplateDetail(models.Model):
    group_id                = models.ForeignKey(Group, on_delete=models.CASCADE)
    form_template_id        = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    legend                  = models.CharField(max_length=5)
    question_line           = models.IntegerField(max_length=15)
    question                = models.CharField(max_length=500)
    is_boolean_question     = models.BooleanField()
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class Inspection01(models.Model):
    template_detail_id      = models.ForeignKey(TemplateDetail, on_delete=models.CASCADE)
    unit_number_id          = models.ForeignKey(UnitNumber, on_delete=models.CASCADE)
    rev                     = models.IntegerField(max_length=3)
    draw_ref                = models.CharField(max_length=15)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass

class Inspection02(models.Model):
    inspection_01_id        = models.ForeignKey(Inspection01, on_delete=models.CASCADE)
    contractor              = models.CharField(max_length=10)
    consultant              = models.CharField(max_length=10)
    consultant_reinspection = models.CharField(max_length=10)
    inspection              = models.CharField(max_length=10)
    reason                  = models.CharField(max_length=200)
    comment                 = models.CharField(max_length=200)
    accept                  = models.BooleanField()
    accept_date             = models.DateTimeField(default=datetime.now, blank=True)
    contractor_name         = models.CharField(max_length=50)
    contractor_date         = models.DateTimeField(default=datetime.now, blank=True)
    consultant_name         = models.CharField(max_length=50)
    consultant_date         = models.DateTimeField(default=datetime.now, blank=True)
    remarks                 = models.CharField(max_length=200)
    is_active               = models.BooleanField()
    creation_time           = models.DateTimeField(default=datetime.now, blank=True)
    creator_user_id         = models.CharField(max_length=50)
    last_modification_time  = models.DateTimeField(default=datetime.now, blank=True)
    last_modifier_user_id   = models.CharField(max_length=50)
    is_deleted              = models.BooleanField()
    deletion_time           = models.DateTimeField(default=datetime.now, blank=True)
    delete_user_id          = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    pass
