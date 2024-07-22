from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    company = models.CharField(max_length=20)
    post = models.CharField(max_length=20)

    def __str__(self):
        return self.username
        # return f"{self.username} {self.company}"
