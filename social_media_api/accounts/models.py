from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # The 'following' field represents users that a user follows
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_set', blank=True)

    def __str__(self):
        return self.username
