from django.db import models

# Create your models here.
class User(models.Model):
    user_name   = models.CharField(max_length=50, unique=True)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    birthday    = models.DateField()
    bio         = models.TextField()
    email       = models.EmailField(unique=True)
    password    = models.CharField(max_length=50)

    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
