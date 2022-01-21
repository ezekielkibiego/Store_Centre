from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, blank=True)
    image = CloudinaryField("image",null=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.location)+']' 

