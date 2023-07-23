from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null = True)
    bio = models.CharField(max_length=140, blank = True)
    phone = models.CharField(max_length=10 , blank = True)

    def __str__(self):
        return f'{self.user.username}\'s profile'