from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_teacher = models.BooleanField()
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile-pictures', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)