from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .models import Post
from .forms import CreatePostForm
from .utils import calculate_time_diff

# CRUD: Create | Retrieve | Update | Delete
def list_posts(request):
    now = datetime.now().astimezone()
    posts_from_db = Post.objects.all()

    time_diff = []
    for post in posts_from_db:
        diff = now - post.updated
        time_diff.append(calculate_time_diff(diff))

    zipped = zip(posts_from_db, time_diff)

    context = {
        'posts': posts_from_db,
        'name': 'Carlos',
        'zipped': zipped,
        'now': now,
    }
    return render(request, 'posts.html', context)

@login_required
def post_detail(request, post_id):
    post_detail = get_object_or_404(Post, id=post_id)
    # post_detail = Post.objects.get(id=post_id)
    context = {
        'post': post_detail
    }
    return render(request, 'post_details.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        my_form = CreatePostForm(request=request, data=request.POST, files=request.FILES)
        if my_form.is_valid():
            my_form.save()
            return redirect('posts:list_posts')
    else:
        my_form = CreatePostForm(request=request)
    context = {
        'form': my_form
    }
    return render(request, 'post_create.html', context)

@login_required
def update_post(request, post_id):
    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CreatePostForm(
            request=request,
            data=request.POST,
            files=request.FILES,
            instance=post
        )
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_id=post.id)
    else:
        form = CreatePostForm(request=request, instance=post)
    context = {
        'id': post_id,
        'update_form': form
    }
    return render(request, 'update_post.html', context)
