"""myWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from myWeb.views import hello_world
from .views import (
    hello_world,
    practice1,
    order_numbers,
    access,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world, name='hello_world'),
    path('practice-1/', practice1, name='practice1'),
    path('orderer-numbers/', order_numbers, name='order_numbers'),
    path('access/<int:edad>/<str:nombre>/', access, name='access'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
