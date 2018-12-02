from django.db import models
from django.contrib.auth.models import User


class No (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contador = models.IntegerField(default=0)
