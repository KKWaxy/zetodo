from typing import Dict

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    title = "ZeTodoApp"
    ctx : Dict = {
        'page_title': title,
    }
    return(render(request=request,context=ctx,template_name='zeapp/tables.html'))

