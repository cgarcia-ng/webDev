from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
def user_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        else:
            error = 'Invalid Credentials'
    context = {
        'error': error
    }
    return render(request, 'login.html', context)