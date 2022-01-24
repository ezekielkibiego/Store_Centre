import email
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_client = models.BooleanField('client status',default=False)
    is_staff = models.BooleanField('staff status',default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    last_login = models.CharField(max_length=1000,null=True)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    last_login = models.CharField(max_length=1000,null=True)


    def __str__(self):
        return f'{self.user}'

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=50,null=True)
    last_login = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return f'{self.user}'



