from .views import *
from django.urls import path

urlpatterns = [
    # elements
    path('elements/', element_list, name='element_list'),
    path('elements/create/', element_create, name='element_create'),
    path('elements/<int:id>/update', element_update, name='element_update'),
    path('elements/<int:id>/delete', element_delete, name='element_delete'),

    # groups
    path('elements/<int:id>/groups', group_list, name='group_list'),
    path('elements/<int:id>/groups/create', group_create, name='group_create'),
    path('groups/<int:id>/update', group_update, name='group_update'),
    path('groups/<int:id>/delete', group_delete, name='group_delete'),

    # number_series
    path('number_series/', number_series_list, name='number_series_list'),
    path('number_series/create', number_series_create, name='number_series_create'),
    path('number_series/<int:id>/update', number_series_update, name='number_series_update'),
    path('number_series/<int:id>/delete', number_series_delete, name='number_series_delete'),

    # forms_type
    path('number_series/<int:id>/forms_type', form_type, name='form_type'),
    path('number_series/<int:id>/forms_type/create', form_type_create, name='form_type_create'),
    path('forms_type/<int:id>/update', form_type_update, name='form_type_update'),
    path('forms_type/<int:id>/delete', form_type_delete, name='form_type_delete'),

    # forms
    path('forms_type/<int:id>/templates', templates, name='templates'),
    path('forms_type/<int:id>/template/create', template_create, name='template_create'),
    path('template/<int:id>/update', template_update, name='template_update'),
    path('template/<int:id>/delete', template_delete, name='template_delete'),
    path('template/<int:id>/newrev', new_rev, name='new_rev'),

    # questions
    path('template/<int:id>/questions', question, name='question'),
    path('template/<int:id>/question/create', question_create, name='question_create'),
    path('template/question/<int:id>/update', question_update, name='question_update'),
    path('template/question/<int:id>/delete', question_delete, name='question_delete'),
    path('template/question/<int:id>/up', move_up, name='move_up'),
    path('template/question/<int:id>/down', move_down, name='move_down'),

    #input
    path('selectform/',select_form,name='select_form'),
    path('selectform/typecode/<int:id>', type_code, name='type_code'),
    path('selectform/typecode/inspection/<int:id>', inspection, name='inspection'),
    path('selectform/typecode/inspection/previous/<int:g>/<int:h>', previous_inspection, name='previous_inspection'),
    path('selectform2/<int:id>', select_form2, name='select_form2'),

]
