from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import redirect, render

from .forms import ProfileUpdateForm
from users.models import Profile

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
    if request.method == "POST":
        username_from_form = request.POST['username']
        if " " in username_from_form:
            return render(request, 'signup.html', {'error': 'Username must not contain spaces'})

        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
            return render(request, 'signup.html', {'error': 'Password doesn not match'})

        try:
            user = User.objects.create_user(
                username=username_from_form,
                password=password
            )
        except IntegrityError:
            return render(
                request,
                'signup.html',
                {'error': f'User {username_from_form} already exists'}
            )

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        # profile = Profile.objects.create(user=user)
        profile = Profile()
        profile.user = user
        profile.save()

        return redirect('users:user_login')

    return render(request, 'signup.html')

def user_profile(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        print("PETICION POST", request.POST)
        print("FORM IS VALID", form.is_valid())
        if form.is_valid():
            data = form.cleaned_data
            print("DATOS DEL FORMULARIO", data)
            # data = {
            #     'phone_number': '123',
            #     'avatar': <InMemoryUploadedFile: 32.jpg (image/jpeg)>,
            #     'website': 'https://google.com'
            # }

            # phone_number = data.get('phone_number')
            if data['avatar']:
                profile.avatar = data['avatar']

            profile.phone_number = data['phone_number']
            profile.website = data['website']
            profile.biography = data['biography']
            profile.save()

    else:
        form = ProfileUpdateForm()

    context = {
        'form': form,
        'profile': profile,
        'user': user
    }

    return render(request, "profile_update.html", context)
