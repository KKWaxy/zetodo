from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm, ChoiceField
from django.forms.utils import ErrorList
from .models import TaskModel

class TaskModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']='form-control'
        
    class Meta:
        model = TaskModel
        fields = ["title","memo","priority","duedate","status"]
