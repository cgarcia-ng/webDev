from django.urls import path

# from myWeb.views import hello_world
from .views import (
    list_posts,
    post_detail,
    create_post,
    update_post,
    search_posts
)

app_name = 'posts'
urlpatterns = [
    # localhost:8000/
    path('', list_posts, name='list_posts'),
    # localhost:8000/post/id
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    # localhost:8000/post/add
    path('post/add/', create_post, name='post_create'),
    # localhost:8000/post/id/edit
    path('post/<int:post_id>/edit', update_post, name='post_update'),
    # localhost:8000/posts/results
    path('posts/results', search_posts, name='search_posts')
]