from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='user_avatars/default.png', upload_to='user_avatars')

    def __str__(self):
        return self.user.username
