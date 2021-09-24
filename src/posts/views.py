from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Post

# CRUD: Create | Retrieve | Update | Delete
# Create your views here.
def list_posts(request):
    if request.user.is_authenticated:
        posts_from_db = Post.objects.all()
        context = {
            'posts': posts_from_db,
            'name': 'Carlos'
        }
        return render(request, 'posts.html', context)
    else:
        return HttpResponseRedirect(reverse('users:user_login'))