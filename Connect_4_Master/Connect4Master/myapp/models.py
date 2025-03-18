# myapp/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.username
