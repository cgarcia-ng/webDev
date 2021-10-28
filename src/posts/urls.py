from django.urls import path

# from myWeb.views import hello_world
from .views import (
    list_posts,
    post_detail
)

app_name = 'posts'
urlpatterns = [
    # localhost:8000/
    path('', list_posts, name='list_posts'),
    # localhost:8000/post/id
    path('post/<int:post_id>/', post_detail, name='post_detail'),

]