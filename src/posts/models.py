from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user        = models.ForeignKey(User, on_delete=models.PROTECT)
    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo       = models.ImageField(upload_to='posts/photos')

    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} created by @{self.user.username}'
