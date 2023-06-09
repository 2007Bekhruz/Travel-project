from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomerUser(AbstractUser):
    avatar = models.ImageField(upload_to='accounts/avatar', blank=True, null=True)
