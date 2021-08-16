from django.http import HttpResponse
from django.shortcuts import render

posts_list = [
    {
        'user': 'Carlos Garcia',
        'image': 'https://picsum.photos/id/237/300/300',
        'description': 'Esta es una descripción',
        'title': 'Conozcan mi mascota Firulays',
    },
    {
        'user': 'Pedro Perez',
        'image': 'https://picsum.photos/300/300',
        'description': 'Esta es otra descripción',
        'title': 'Mi viaje a Paris',
    },
]


def hello_world(request):
    resultado = 4 + 5
    context = {
        'nombre': 'Carlos',
    }
    return render(request, 'index.html', context)
    # return HttpResponse('<h1>Hola Mundo. Mi nombre es Carlos</h1>')

def practice1(request):
    return render(request, 'practice-1.html')

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

def posts(request):
    context = {
        'posts': posts_list
    }
    return render(request, 'posts.html', context)
    # content = []
    # for post in data:
    #     content.append(
    #         f"""
    #         <h1>{post.get("title")}</h1>
    #         <figure><img src='{post.get("image")}'></figure>
    #         <p><strong>Descripción: </strong>{post.get("description")}</p>
    #         <p><strong>Creado por: </strong>{post.get("user")}</p>
    #         """
    #     )
        # <h1>{post["title"]}</h1>
    # return HttpResponse("<br>".join(content))
