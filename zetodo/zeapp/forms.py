from django.forms import ModelForm, forms
from .models import TaskModel

class TaskModelForm(ModelForm):
    
    class Meta:
        model = TaskModel
        fields = ["title","memo","priority","duedate","status"]
