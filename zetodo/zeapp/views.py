from typing import Dict

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    ctx : Dict = {
        'title': "Todo 1",
        'description' :"Todo liste 1"
    }
    return(render(request=request,context=ctx,template_name='index.html'))