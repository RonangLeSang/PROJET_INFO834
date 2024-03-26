from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    id = models.CharField(primary_key=True, max_length=24)
