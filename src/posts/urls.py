from django.urls import path

# from myWeb.views import hello_world
from .views import (
    list_posts,
)

app_name = 'posts'
urlpatterns = [
    path('', list_posts, name='list_posts'),
]