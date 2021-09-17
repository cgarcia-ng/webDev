from django.urls import path

# from myWeb.views import hello_world
from .views import (
    list_posts,
)

urlpatterns = [
    path('', list_posts),
]