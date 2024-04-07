from typing import Dict
from uuid import UUID

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

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
        else:
            messages.error(request, form.errors)
    tasks = TaskModel.objects.all()
    ctx['tasks'] = tasks
    
    return(render(request=request,context=ctx,template_name='zeapp/index.html'))

def delete_task(request: HttpRequest, task_id: UUID) -> HttpResponse:

    task = get_object_or_404(TaskModel, pk=task_id)
    task.delete()

    return(redirect('index', permanent=True))

def update_task(request: HttpRequest, task_id: UUID) -> HttpResponse:
    pass

def task_detail(request: HttpRequest, task_id: UUID) -> HttpResponse:
    
    task = get_object_or_404(TaskModel, pk=task_id)
    
    if request.method == "POST":
        if request.POST['title']:
            task.title = request.POST['title']
        if request.POST['memo']:
            task.memo = request.POST['memo']
        if request.POST['priority']:
            task.priority = request.POST['priority']
        if request.POST['status']:
            task.status = request.POST['status']
        if request.POST['duedate']:
            task.duedate = request.POST['duedate']
        task.save()
        return(redirect('index', permanent=True))
        
    form = TaskModelForm(instance=task)

    ctx : Dict = {
        'page_title' : 'Task detail-'+str(task.id),
        'task' : task,
        'form' : form,
    }

    return(render(request=request, context=ctx, template_name='zeapp/index.html'))
