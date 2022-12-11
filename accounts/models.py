from django.contrib.auth.models import AbstractUser
from django.db import models

from .accountmanager import CodePouceAccountManager


class CodePouceUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    photo = models.TextField(blank=True)
    telephone = models.CharField(max_length=40)
    date_naissance = models.DateField()
    langues = models.JSONField()
    ville = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CodePouceAccountManager()

    def __str__(self):
        return self.email
