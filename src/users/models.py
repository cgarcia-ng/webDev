from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday    = models.DateField()
    biography   = models.TextField()
    phone_number = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='users/avatars', null=True, blank=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
        # return f'{self.user.first_name} {self.user.last_name}'

    # Object(1)


