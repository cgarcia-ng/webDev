from django.urls import path

from .views import (
    user_login,
)

app_name = 'users'
urlpatterns = [
    # localhost:8000/users/login/
    path('login/', user_login, name='user_login'),
]