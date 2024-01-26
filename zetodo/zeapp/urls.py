from django.urls import path
from zeapp.views import index

urlpatterns = [
    path('',view=index,name='index')
]