from typing import Dict

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import TaskModelForm
from .models import TaskModel


def index(request: HttpRequest) -> HttpResponse:

    title = "ZeTodoApp"

    ctx : Dict = {
        'page_title': title
        }
    
    if(request.method == 'POST'):
        form = TaskModelForm(request.POST)
        if(form.is_valid()):
            form.save()
            tasks = TaskModel.objects.all()
            ctx['tasks'] = tasks
            return(render(request=request,context=ctx,template_name='zeapp/index.html'))
        else:
            raise Exception(form.errors.as_json())
    else:
        tasks = TaskModel.objects.all()
        ctx['tasks'] = tasks
        return(render(request=request,context=ctx,template_name='zeapp/index.html'))

