from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    resultado = 4 + 5
    context = {
        'nombre': 'Carlos',
    }
    return render(request, 'templates/index.html', context)
    # return HttpResponse('<h1>Hola Mundo. Mi nombre es Carlos</h1>')

def practice1(request):
    return render(request, 'templates/practice-1.html')

def order_numbers(request):
    # import pdb; pdb.set_trace()
    # numbers = request.GET.get('numbers').split(',')
    # order_numbers = []
    # for number in numbers:
    #     order_numbers.append(int(number))
    # ordered_numbers = sorted(order_numbers)

    # List comprenhension
    ordered_numbers = sorted(
        [int(number) for number in request.GET.get('numbers').split(',')]
    )
    return HttpResponse(f'<h1>Lista ordernada de números: {ordered_numbers}<h1/>')

def access(request, edad, nombre):
    if edad < 12:
        return HttpResponse('<h1>Lo siento no puedes ingresar en esta pagina web<h1/>')
    else:
        return HttpResponse(f'<h1>Hola {nombre}, bienvenido de vuelta<h1/>')
