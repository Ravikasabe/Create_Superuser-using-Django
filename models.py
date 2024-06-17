
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class GFG(AbstractUser):
    phone = models.CharField(max_length=12, unique=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']  # Add email to required fields if necessary
    objects = UserManager()

    def __str__(self):
        return self.phone
