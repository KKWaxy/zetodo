from django.forms import ModelForm, DateInput

from .models import TaskModel

class TaskDateInput(DateInput):
    input_type = "date"
    

class TaskModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']='form-control'
        
    class Meta:
        model = TaskModel
        fields = ["title","memo","priority","duedate","status"]
        widgets = {
            "duedate": TaskDateInput(format="dd/mm/yyyy"),
        }