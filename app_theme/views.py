from django.shortcuts import render
from django.http import HttpResponse

def faylni_oqish(request):
    with open('123.txt', 'r') as f:
        content = f.read()
    content_with_br = "<br>".join(content.split("\n"))
    return HttpResponse(content_with_br)
