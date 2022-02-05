from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


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

    def get_image_url(self):
        return f'{settings.MEDIA_URL}{self.photo}'

    def get_time_diff(self):
        diff = datetime.now().astimezone() - self.updated
        days = diff.days
        hours = diff.seconds // 3600
        minutes = int((diff.seconds / 3600 - hours) * 60)
        years = days // 365

        if days != 0:
            if days == 1:
                # text = "Last updated {ducks}".format(ducks=days)
                text = f"Last updated {days} day, {hours} hours and {minutes} minutes"
            else:
                text = f"Last updated {days} days, {hours} hours and {minutes} minutes"
        else:
            if hours == 1:
                text = f"Last updated {hours} hour and {minutes} minutes"
            elif hours == 0:
                text = f"Last updated {minutes} minutes and {diff.seconds} seconds"

        return text
