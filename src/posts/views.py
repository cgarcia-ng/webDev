from django.shortcuts import render

from .models import Post

# CRUD: Create | Retrieve | Update | Delete
# Create your views here.
def list_posts(request):
    posts_from_db = Post.objects.all()
    context = {
        'posts': posts_from_db,
        'name': 'Carlos'
    }
    return render(request, 'posts.html', context)