from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_image')
    cover_image = models.ImageField(default='default2.jpg', upload_to='cover_image')
    formal_image = models.ImageField(default='default2.jpg', upload_to='formal_image')

    def __str__(self):
        return f'{self.user.username} profile image'




