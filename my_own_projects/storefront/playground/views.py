from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('Hello World!')

def hello(request):
    return render(request, 'playground/hello.html', {'name' : 'Rabin'})

