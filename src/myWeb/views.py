from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    resultado = 4 + 5
    context = {
        'nombre': 'Carlos',
        'suma': resultado
    }
    return render(request, 'templates/index.html', context)
    # return HttpResponse('<h1>Hola Mundo. Mi nombre es Carlos</h1>')

def practice1(request):
    return render(request, 'templates/practice-1.html')