from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import Post

# CRUD: Create | Retrieve | Update | Delete
# Create your views here.
def list_posts(request):
    #if request.user.is_authenticated:
    posts_from_db = Post.objects.all()
    context = {
        'posts': posts_from_db,
        'name': 'Carlos'
    }
    return render(request, 'posts.html', context)
    #else:
        #return HttpResponseRedirect(reverse('users:user_login'))

@login_required
def post_detail(request, post_id):
    post_detail = get_object_or_404(Post, id=post_id)
    # post_detail = Post.objects.get(id=post_id)
    context = {
        'post': post_detail
    }
    return render(request, 'post_details.html', context)