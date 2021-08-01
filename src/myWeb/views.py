from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, 'templates/index.html')
    # return HttpResponse('<h1>Hola Mundo. Mi nombre es Carlos</h1>')