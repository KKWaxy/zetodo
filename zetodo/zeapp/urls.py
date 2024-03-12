from .views import index, delete_task

from django.urls import path



urlpatterns = [
    path('',view=index,name='index'),
    path('delete/<uuid:task_id>', view=delete_task, name='delete_task'),
]