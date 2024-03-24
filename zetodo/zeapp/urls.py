from .views import index, delete_task, task_detail

from django.urls import path



urlpatterns = [
    path('',view=index,name='index'),
    path('delete/<uuid:task_id>', view=delete_task, name='delete_task'),
    path('task_detail/<uuid:task_id>', view=task_detail, name='task_detail')
]