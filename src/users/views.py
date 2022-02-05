from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

# Create your views here.
def user_login(request):
    error = ''
    # if request.user.is_authenticated:
    #     return redirect ('posts:list_posts')
    # else:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next:
                return redirect(next)
            else:
                return redirect('posts:list_posts')
        else:
            error = 'Invalid Credentials'

    context = {
        'error': error
    }
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect("posts:list_posts")

def user_signup(request):
    return render(request, "signup.html")
