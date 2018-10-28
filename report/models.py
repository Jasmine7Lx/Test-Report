from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=100, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta(AbstractUser.Meta):
        pass